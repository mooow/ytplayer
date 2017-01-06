#!/usr/bin/env python3

import threading
import ytlib

class UI():
    def __init__(self, on_next_song = None):
        self.ids = []
        self.sem = threading.Semaphore(value = 0)
        self.killed = threading.Lock()
        self.thread_player = ytlib.Player(self.ids, self.sem, self.killed, on_next_song)
    
    def main(self):
        self.thread_player.start()
    
    def download(self, search_string):
        search_string = search_string.strip()
        if len(search_string) <= 0: return
        res = ytlib.search1(search_string)
        ytlib.Downloader(self.ids, self.sem, res).start()
        return res
    
    def close(self):
        print("\n\nAsking threads to terminate gracefully...", end="")
        self.killed.acquire(False)
        self.sem.release()
        self.thread_player.join()
        print("done")
        exit(0)
