# ytplayer
A youtube-based music player!

## How does it work?
You type the name of the song you want to hear (as if you were searching it on YouTube...)
and then it will be put in a queue. The songs will be played sequentially.

## How do you do that?
We use search what you type on youtube, fetch the first link and then we use
[youtube_dl](https://github.com/rg3/youtube-dl) (which must be installed on your system) to download
the audio file, which is then played with gstreamer (which must be installed on your system, but can be
replaced by whatever player you want)

## Licensing, Author
ytplayer is Copyright (C) 2016 of Lorenzo Mureu (more information can be found on the `LICENSE` file)

## Dependencies
This program has the following dependencies:
* python3
* PyQt5
* python-lxml
* python-urllib3
* youtube-dl
* gstreamer (gst-play-1.0)

On ArchLinux you should be able to install them by running:
```
pacman -S --needed python python-urllib3 python-pyqt5 python-lxml youtube-dl gst-plugins-base-libs
```
    
## Compilation
Before running `ytplayer`, if you want to use the GUI, you **MUST** run `make` beforehand

## TODO
1. Avoid doing things with os.system
2. Use a dedicated temp folder (instead of current working directory)
3. Add a GUI
