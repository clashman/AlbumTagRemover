#!/usr/bin/env python3

import os
import sys
import mutagen.id3

def writePlaylist(dirpath, filenames):
    m3uExt = ".m3u"
    m3ufilename = os.path.join(dirpath, os.path.basename(dirpath)) + m3uExt
    with open(m3ufilename, 'w') as playlist:
        for filename in filenames:
            if filename[0] != "." and os.path.splitext(filename)[1] != m3uExt:
                playlist.write(filename + "\n")

for path in sys.argv[1:]:
    for dirpath, dirnames, filenames in os.walk(path):
        album = os.path.basename(os.path.abspath(dirpath))
        talb = mutagen.id3.TALB(text=album)
        print("Walking {}:".format(dirpath))
        print("added playlist")
        writePlaylist(dirpath, filenames)
        for filename in filenames:
            sys.stdout.write(" tagging {}".format(filename))
            try:
                song_path = os.path.join(dirpath, filename)
                song = mutagen.id3.ID3(song_path)
                song.delall("TALB")
                #song.add(talb)
                song.save()
                print()
            except:
                print(" skipped (no id3 tags)")
