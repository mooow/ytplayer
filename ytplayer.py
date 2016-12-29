#!/usr/bin/env python3

import ytlib
import youtube_dl
import threading
import os
from time import sleep
import tempfile

PLAYER = 'gst-play-1.0'

def download(res):
    print("Putting: {0}".format( ytlib.tostring(res) ))
    ydl_opts = {'format' : 'bestaudio', 'outtmpl': '%(id)s.tmp', 'quiet': True}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([ res['url'] ])

def main():
    tmpdir = tempfile.TemporaryDirectory(prefix = "ytplayer-")
    os.chdir(tmpdir.name)
    print("Using tmpdir: {0}".format(tmpdir.name))
    ids = []
    sem = threading.Semaphore(value = 0)
    killed = threading.Lock()
    thread = Player(ids, sem, killed)
    thread.start()
    while True:
        try:    
            s = input("query? ").strip()
            if len(s) == 0: continue
            res = ytlib.search1(s)
            Downloader(ids, sem, res).start()
        except KeyboardInterrupt:
            print("\n\nAsking threads to terminate gracefully...", end="")
            killed.acquire(False)
            sem.release()
            thread.join()
            print("done")
            exit(0)
        except IndexError:
            print("Not found")

class Player(threading.Thread):
    def __init__(self, ids, sem, killed):
        threading.Thread.__init__(self)
        self.ids = ids
        self.sem = sem
        self.killed = killed
        
    def play(self):
        self.sem.acquire()
        if self.killed.locked():
            exit(0)
        obj = self.ids.pop(0)
        print("Thread doing: {0}".format(ytlib.tostring(obj)))
        ret = os.system("{0} {1}.tmp </dev/null >/dev/null".format(PLAYER, obj['id']))  # TODO: use another way
        os.system("rm {0}.tmp".format(obj['id']))                                 # TODO: use another way
        if ret != 0:
            print("[PLAYER] Player stopped")
    
    def run(self):
        while True: 
            self.play()

class Downloader(threading.Thread):
    def __init__(self, ids, sem, res):
        threading.Thread.__init__(self)
        self.ids = ids
        self.sem = sem 
        self.res = res
    
    def run(self):
        print("Downloading {0}".format( ytlib.tostring(self.res) ))
        ydl_opts = {'format' : 'bestaudio', 'outtmpl': '%(id)s.tmp', 'quiet': True}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([ self.res['url'] ])
        self.ids.append(self.res)
        self.sem.release()

if __name__ == '__main__':
    main()
    
