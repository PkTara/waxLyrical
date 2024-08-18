from lyricsgenius import Genius
from lyricsgenius import PublicAPI
import json
from lyricAnalyser import analyse


with open("geniusToken.txt", "r") as file:
   accessToken= file.read()
genius = Genius(accessToken)

def genLyrics(genius, songURL):
   lyrics = genius.lyrics(song_url=songURL)
   return(lyrics)


# getting song ID
song = genius.search_songs("8 Kambarys save")
songID = song["hits"][0]["result"]["api_path"]
songID = songID.split("/")[2]

songCoverLink = song["hits"][0]["result"]["song_art_image_url"]



# into dictionary for json
songInfo = {}
songInfo["songCoverLink"] = songCoverLink
songInfo["lyrics"] = genLyrics(genius, "https://genius.com/8-kambarys-deginu-save-lyrics")

# print(songInfo)

from lyricAnalyser import analyse

songInfo["graph"] = analyse( songInfo["lyrics"] )


# # Serializing json
# json_object = json.dumps(songInfo, indent=4)
 

from databaseWrite import writeJSON
writeJSON(songInfo)

    
