from Playlist import Playlist
from Song import Song
import os

class Player:

    def __init__(self) -> None:
        pass

    def play(self, item):
        if isinstance(item, Song):
            # play song
            print("Playing : {}".format(item.get_prop("title")))
            os.system("mpv {} --no-video".format(item.get_link()))
            return
        if isinstance(item, Playlist):
            # play playlist
            return