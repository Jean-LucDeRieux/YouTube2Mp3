#    Author Name: Jean-Luc DeRieux
#   Date Created: 02/20/2023
#          About: Creates a mp3 audio download from Youtube. Meant for easily finding audio for video production.
#  Last Modified: 02/20/2023
#       Modified:


# Importing libraries
from pytube import YouTube
import os

# User inputs URL
url = input('Enter youtube url :  ')
video = YouTube(url)

# Converting URL to audio format
out_path = video.streams.filter(only_audio=True).first().download()
new_name = os.path.splittext(out_path)

# Saving audio clip as mp3
os.rename(out_path, new_name[0] + '.mp3')


# Found outline of code on this youtube short: https://youtube.com/shorts/GCJ89P4Yukg?feature=share
