# ytplayer
A youtube-based music player!

## How does it work?
You type the name of the song you want to hear (as if you were searching it on YouTube...)
and then it will be put in a queue. The songs will be played sequentially.

## How do you do that?
We use search what you type on youtube, fetch the first link and then we use
[https://github.com/rg3/youtube-dl](youtube_dl) (which must be installed on your system) to download
the audio file, which is then played with gstreamer (which must be installed on your system, but can be
replaced by whatever player you want)

## Licensing, Author
ytplayer is Copyright (C) 2016 of Lorenzo Mureu (more information can be found on the `LICENSE` file)

## TODO
1. Avoid doing things with os.system
2. Use a dedicated temp folder (instead of current working directory)
3. Add a GUI
