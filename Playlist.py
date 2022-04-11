from os import system
from Config import PlaylistPrefix, SongProperties, SongSearchProp
from Song import Song
import random


class Playlist:

    def __init__(self, name: str = "no_name", old_list = []) -> None:
        self.__list = old_list
        self.__name = name

    def __str__(self) -> str:
        list_str = ""
        for song in self.__list:
            list_str += str(song) + "\n"
        return list_str
    
    def __len__(self) -> int:
        return len(self.__list)
    
    def getName(self) -> str:
        return self.__name
    
    def get(self, id: str) -> Song:
        for song in self.__list:
            if song.get_prop("id") == id:
                return song
        return None
    
    def exist(self, song: Song) -> bool:
        return song in self.__list

    def add(self, song: Song) -> bool:
        # check for duplicates
        if self.exist(song):
            return False
        
        # add to list
        self.__list.append(song)
        return True

    def remove(self, song: Song) -> bool:
        if not self.exist(song):
            return False
        # remove from list
        self.__list.remove(song)
        return True
    
    def removeById(self, id: str) -> bool:
        song =  self.get(id)
        if song:
            return self.remove(song)
        return False
    
    def get_link(self, shuffle: bool = False) -> str:
        id_list = [ song.get_prop("id") for song in self.__list ]
        if shuffle:
            id_list = random.shuffle(id_list)
        return PlaylistPrefix + ",".join(id_list)
    
    def getAll(self) -> list:
        return self.__list
    
    def search(self, term: str, prop:str = SongSearchProp):
        if not prop in SongProperties:
            return None
        result = []
        for song in self.__list:
            if term.lower() in song.get_prop(prop).lower():
                result.append(song)
        return Playlist("result: " + term, result)
