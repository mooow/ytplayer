#!/usr/bin/env python3

import urllib.request, lxml.html

YOUTUBE_BASE_URL = 'https://www.youtube.com'
YOUTUBE_SEARCH_URL = YOUTUBE_BASE_URL + '/results?search_query={0}' 
XPATH_SEARCH_RESULTS = '//a[contains(@class, "yt-uix-tile-link")]'

def html_get(url):
    obj = urllib.request.urlopen(url)
    return lxml.html.parse(obj)

def search(string):
    string = urllib.parse.quote_plus(string)        # escape the string :)
    url = YOUTUBE_SEARCH_URL.format(string)         # get search url
    obj = html_get(url)
    global results
    results = []
    for item in obj.xpath(XPATH_SEARCH_RESULTS):
        res = {}
        res['title'] = item.get('title')
        res['url'] = YOUTUBE_BASE_URL + item.get('href')
        try:
            res['id'] = _get_id(item.get('href'))
            results.append(res)
        except KeyError:pass
            #print("[WARNING] Could not parse url {0}, skipping...".format(item.get('href')))
    return results

def _get_id(url):
    query = urllib.parse.urlsplit(url).query
    return urllib.parse.parse_qs(query)['v'][0]

def search1(string):
    return search(string)[0]

def tostring(item):
    return "{0} [{1}]".format(item['title'], item['id'])



import threading
import os
import youtube_dl

class Player(threading.Thread):
    def __init__(self, ids, sem, killed, on_next_song = None, player = "gst-play-1.0"):
        threading.Thread.__init__(self)
        self.ids = ids
        self.sem = sem
        self.killed = killed
        self.player = player
        self.on_next_song = on_next_song
    
    def event_next_song(self, res):
        if self.on_next_song:
            self.on_next_song(res)
    
    def play(self):
        self.sem.acquire()
        if self.killed.locked():
            exit(0)
        obj = self.ids.pop(0)
        self.event_next_song(obj)
        print("Thread doing: {0}".format(tostring(obj)))
        ret = os.system("{0} {1}.tmp </dev/null >/dev/null".format(self.player, obj['id']))  # TODO: use another way
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
        print("Downloading {0}".format(tostring(self.res) ))
        ydl_opts = {'format' : 'bestaudio', 'outtmpl': '%(id)s.tmp', 'quiet': True}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([ self.res['url'] ])
        print("Download finished for {0}".format(self.res['id']))
        self.ids.append(self.res)
        self.sem.release()
