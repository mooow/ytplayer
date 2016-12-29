#!/usr/bin/env python3

import ytlib
import youtube_dl
import threading
import os
from time import sleep

PLAYER = 'gst-play-1.0'

def download(res):
    print("Putting: {0}".format( ytlib.tostring(res) )
    ydl_opts = {'format' : 'bestaudio', 'outtmpl': '%(id)s.tmp', 'quiet': True}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([ res['url'] ])

def main():
    ids = []
    sem = threading.Semaphore(value = 0)
    thread = Player(ids, sem)
    thread.start()
    while True:
        s = input("query? ")
        res = ytlib.search1(s)
        download(res)
        ids.append(res)
        sem.release()

class Player(threading.Thread):
    def __init__(self, ids, sem):
        threading.Thread.__init__(self)
        self.ids = ids
        self.sem = sem 
        
    def play(self):
        self.sem.acquire()
        obj = self.ids.pop(0)
        print("Thread doing: {0}".format(ytlib.tostring(res))
        os.system("{0} {1}.tmp </dev/null >/dev/null".format(PLAYER, obj['id']))  # TODO: use another way
        os.system("rm {0}.tmp".format(obj['id']))                                 # TODO: use another way
    
    def run(self):
        while True: 
            self.play()
        

if __name__ == '__main__':
    main()
