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

def play(audio_objects, songs_list):
    selected_index = songs_list.curselection()
    if selected_index:
        selected_index = selected_index[0]
        song_path = audio_objects[selected_index].get_path()
        print(song_path)
        mixer.music.load(song_path)
        mixer.music.play()

def pause():
    mixer.music.pause()

def stop(songs_list):
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

def resume():
    mixer.music.unpause()

path_path = "database/paths.txt"
audio_objects = create_audio_objects(path_path)

root = Tk()
root.title('DataFlair Music player App ')
mixer.init()

songs_list = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('arial', 15), height=12, width=47,
                    selectbackground="gray", selectforeground="black")
songs_list.grid(columnspan=9)

# Populate the Listbox with song names
for audio in audio_objects:
    songs_list.insert(END, audio.name)  # Assuming 'title' is the attribute with the song name

defined_font = font.Font(family='Helvetica')

play_button = Button(root, text="Play", width=7, command=lambda: play(audio_objects, songs_list))
play_button['font'] = defined_font
play_button.grid(row=1, column=0)

pause_button = Button(root, text="Pause", width=7, command=pause)
pause_button['font'] = defined_font
pause_button.grid(row=1, column=1)

stop_button = Button(root, text="Stop", width=7, command=lambda: stop(songs_list))
stop_button['font'] = defined_font
stop_button.grid(row=1, column=2)

resume_button = Button(root, text="Resume", width=7, command=resume)
resume_button['font'] = defined_font
resume_button.grid(row=1, column=3)

mainloop()
