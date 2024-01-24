from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

class Button(Button):
    def __init__(self, root, image_path, command):
        self.img = PhotoImage(file=image_path).subsample(3)
        super().__init__(root, image=self.img, bg="#0f1a2b", command=command)

def load_artist_songs(artist_folder):
    global ar_f
    ar_f = artist_folder
    playlist_box.delete(0, tk.END)
    artist_folder_path = os.path.join("database", artist_folder)
    
    if os.path.exists(artist_folder_path) and os.path.isdir(artist_folder_path):
        songs = [f for f in os.listdir(artist_folder_path) if f.lower().endswith('.mp3') and os.path.isfile(os.path.join(artist_folder_path, f))]
        for song in songs:
            playlist_box.insert(tk.END, song)
    else:
        playlist_box.insert(tk.END, "Folder not found")

def extract_data(current_song_name):
    path = os.path.join("database", ar_f, f"{current_song_name}.txt")

    with open(path) as temp_read:
        publisher = temp_read.readline().split(';')[1].split('\n')[0]
        title = temp_read.readline().split(';')[1].split('\n')[0]
        date = temp_read.readline().split(';')[1].split('\n')[0]
        duration = temp_read.readline().split(';')[1].split('\n')[0]
        album = temp_read.readline().split(';')[1].split('\n')[0]

    info_label.config(text=f"Publisher: {publisher}\nTitle: {title}\nDate: {date}\nDuration: {duration} seconds\nAlbum: {album}\n")

def on_song_select(event):
    selected_index = playlist_box.curselection()
    if selected_index:
        selected_song = playlist_box.get(selected_index)
        extract_data(selected_song)

def play_music():
    global current_song_name
    selected_song = playlist_box.get(tk.ACTIVE)
    if selected_song:
        current_song_name = selected_song
        artist = selected_song.split(" ")[0]
        song_path = os.path.join("database", artist, selected_song)
        mixer.music.load(song_path)
        mixer.music.play()

def pause_music():
    if mixer.music.get_busy():
        mixer.music.pause()

def stop_music():
    mixer.music.stop()

def next_music():
    current_index = playlist_box.curselection()
    next_index = current_index[0] + 1 if current_index else 0
    if next_index < playlist_box.size():
        playlist_box.selection_clear(0, tk.END)
        playlist_box.selection_set(next_index)
        play_music()

def prev_music():
    current_index = playlist_box.curselection()
    prev_index = current_index[0] - 1 if current_index else 0
    if prev_index >= 0:
        playlist_box.selection_clear(0, tk.END)
        playlist_box.selection_set(prev_index)
        play_music()

root = Tk()
root.title("<#")
root.geometry("900x600")
root.configure(bg="#0f1a2b")
root.resizable(False, False)

mixer.init()

logo_img = PhotoImage(file="img/logo.png")
root.iconphoto(False, logo_img)
bgrnd = PhotoImage(file="img/bgrnd.png").subsample(3)
Label(root, image=bgrnd).pack()

info_label = Label(root, text="", font=("Helvetica", 14), bg="#0f1a2b", fg="white")
info_label.place(x=10, y=450, width=400, height=100)

# instances of buttons
tublatanka_btn = Button(root, "img/tublatanka.png", lambda: load_artist_songs("tublatanka"))
metallica_btn = Button(root, "img/metallica.png", lambda: load_artist_songs("metallica"))
gunsnroses_btn = Button(root, "img/gunsnroses.png", lambda: load_artist_songs("gunsnroses"))
radiohead_btn = Button(root, "img/radiohead.png", lambda: load_artist_songs("radiohead"))
rhchp_btn = Button(root, "img/rhchp.png", lambda: load_artist_songs("rhchp"))

# placing buttons
tublatanka_btn.place(x=800, y=100)
metallica_btn.place(x=800, y=200)
gunsnroses_btn.place(x=800, y=300)
radiohead_btn.place(x=800, y=400)
rhchp_btn.place(x=800, y=500)

playlist_box = tk.Listbox(root, selectbackground="light grey", selectmode=tk.SINGLE)
playlist_box.place(x=10, y=10, width=400, height=400)


play_btn = Button(root, "img/play.png", play_music)
play_btn.place(x=505, y=10)

pause_btn = Button(root, "img/pause.png", pause_music)
pause_btn.place(x=605, y=10)

stop_btn = Button(root, "img/stop.png", stop_music)
stop_btn.place(x=705, y=10)

next_btn = Button(root, "img/forward.png", next_music)
next_btn.place(x=705, y=10)

prev_btn = Button(root, "img/backward.png", prev_music)
prev_btn.place(x=805, y=10)

playlist_box.bind("<ButtonRelease-1>", on_song_select)

root.mainloop()
