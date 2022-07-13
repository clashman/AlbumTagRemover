# AlbumTagRemover
* Removes ID3 album tags (TALB) from music files so Spotlight opens individual files instead of the whole album in macOS.
* Adds [foldername].m3u so that all music in a folder can be opened with a music player.

# Dependencies
`pip3 install mutagen`

# Usage
`./id3_talb_remove.py ~/Music/folder [~/Music/more_folders]`
