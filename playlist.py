from pytube import Playlist
import subprocess
import glob
import re
import os
import tempfile


if not os.path.isdir("./mp3"):
  os.mkdir("mp3") 

path_dwn = os.path.join(os.getcwd(), "mp3")

playlist_url = input("Insert Youtube URL: ")

playlist = Playlist(playlist_url)
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")    


def playlist2mp3(playlist, path_dwn):
  for video in playlist.videos:
    try:
      name = re.sub(r"[^0-9a-zA-Z]+",r'_',video.title)+'.mp4'
      
      filename = video.streams.get_audio_only().download(tempfile.gettempdir(), filename=name)

      output_path = os.path.join(path_dwn, os.path.splitext(name)[0] + '.mp3')
      
      command = "ffmpeg -i " + filename + " -ab 160k -ac 2 -ar 44100 -vn " + output_path
      os.system(command)
      
      os.remove(filename)

    except:
      print("An exception occurred")


playlist2mp3(playlist, path_dwn)



      
