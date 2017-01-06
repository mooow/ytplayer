#!/usr/bin/env python3

import ytlib
import os
import tempfile
from cli import CLI
from gui import GUI

#def download(res):
    #print("Putting: {0}".format( ytlib.tostring(res) ))
    #ydl_opts = {'format' : 'bestaudio', 'outtmpl': '%(id)s.tmp', 'quiet': True}
    #with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #ydl.download([ res['url'] ])

def main():
    tmpdir = tempfile.TemporaryDirectory(prefix = "ytplayer-")
    os.chdir(tmpdir.name)
    print("Using tmpdir: {0}".format(tmpdir.name))
    GUI().main()
    print("done")

if __name__ == '__main__':
    main()
