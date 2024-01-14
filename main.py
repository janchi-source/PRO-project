import os
import tkinter
from tkinter import filedialog, ttk
from pygame import mixer
# from functions import *
# import functions as f
from kate import *

root = tkinter.Tk()
root.title("Music Player")

mixer.init()


albums = Albums()
albums.create_album()


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




c = tkinter.Canvas(root, width=800, height=600, background="#191414")
c.pack()

c.create_rectangle(0, 0, 820, 60, fill="grey", outline="black")
c.create_rectangle(0, 540, 820, 610, fill="grey")
play_button = c.create_oval(375, 545, 425, 595, fill="light grey", width=4, outline="black")
prev_button = c.create_oval(345, 557, 370, 582, fill='light grey', width=3, outline='black')
next_button = c.create_oval(432, 557, 457, 582, fill='light grey', width=3, outline="black")

sound_button = tkinter.Button(root, text="Play Sound", command=play)
sound_button.place(relx=0.5, rely=0.5, anchor="center")

entry_search = tkinter.Entry(root, width=20)
entry_search.place(x=10, y=10)

search_button = tkinter.Button(root, text="Load Songs From Folder", command=on_search_click)
search_button.place(x=150, y=10)

playlist_box = tkinter.Listbox(root, selectbackground="light grey", selectmode=tkinter.SINGLE)
playlist_box.place(x=10, y=60, width=780, height=470)

c.tag_bind(prev_button, '<ButtonPress-1>', lambda event: on_prev_click())
c.tag_bind(next_button, '<ButtonPress-1>', lambda event: on_next_click())

root.mainloop()
