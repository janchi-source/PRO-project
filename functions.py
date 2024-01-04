# import winsound as ws
from audio import Audio
from song import Song
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog

def create_audio_objects(path_path):
    with open(path_path, 'r') as paths_file:
        file_paths = paths_file.read().splitlines()
    audio_objects = [Audio(path) for path in file_paths]
    return audio_objects

def Play(audio):
    song = audio.get(ACTIVE)
    song = f'database/{song}'
    mixer.music.load(song)
    mixer.music.play()

def Pause():
    mixer.music.pause()

# def Stop():
#     mixer.music.stop()
#     songs_list.selection_clear(ACTIVE)

#to resume the song

def Resume():
    mixer.music.unpause()
