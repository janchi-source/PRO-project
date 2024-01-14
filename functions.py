import os
import tkinter
from tkinter import filedialog, ttk
from pygame import mixer


playlist = []

i = 0
def play():
    if playlist:
        current_song = playlist[0]
        mixer.music.load(current_song["paths"][i])
        mixer.music.play()

def on_prev_click():
    current_song_index = playlist.curselection()
    if current_song_index:
        prev_index = (current_song_index[0] - 1) % len(playlist)
        playlist_box.selection_clear(0, tkinter.END)
        playlist_box.selection_set(prev_index)
        playlist_box.activate(prev_index)
        play()
        i -= 1

def on_next_click():
    current_song_index = playlist_box.curselection()
    if current_song_index:
        next_index = (current_song_index[0] + 1) % len(playlist)
        playlist_box.selection_clear(0, tkinter.END)
        playlist_box.selection_set(next_index)
        playlist_box.activate(next_index)
        play()
        i += 1

def on_search_click():
    folder_path = filedialog.askdirectory(title="Select Music Folder")
    if folder_path:
        load_songs_from_folder(folder_path)

def load_songs_from_folder(folder_path):
    try:
        global playlist
        playlist = []

        for file_name in os.listdir(folder_path):
            if file_name.lower().endswith(('.mp3', '.wav', '.ogg')):
                song_path = os.path.join(folder_path, file_name)
                playlist.append({"name": file_name, "paths": [song_path]})

        playlist_box.delete(0, tkinter.END)
        for song_info in playlist:
            playlist_box.insert(tkinter.END, song_info["name"])
    except Exception as e:
        tkinter.messagebox.showerror("Error", f"Error loading songs from folder: {str(e)}")
