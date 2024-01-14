from audio import Audio
from song import Song
import functions as f
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog

path_path = "database/paths.txt"
audio_objects = f.create_audio_objects(path_path)

print(audio_objects)

root = Tk()
root.title('main')
mixer.init()

#create the listbox to contain songs
songs_list=Listbox(root,selectmode=SINGLE,bg = "black",fg = "white",font = ('arial',15),height = 12,width = 47,selectbackground = "gray",selectforeground = "black")
songs_list.grid(columnspan=9)
 
defined_font = font.Font(family = 'Helvetica')

#play button
play_button = Button(root,text = "Play",width = 7,command = f.Play)
play_button['font'] = defined_font
play_button.grid(row = 1,column = 0)

#pause button 
pause_button = Button(root,text = "Pause",width = 7,command = f.Pause)
pause_button['font'] = defined_font
pause_button.grid(row = 1,column = 1)

#stop button
# stop_button=Button(root,text="Stop",width =7,command=f.Stop)
# stop_button['font']=defined_font
# stop_button.grid(row=1,column=2)

#resume button
Resume_button = Button(root,text="Resume",width = 7,command = f.Resume)
Resume_button['font'] = defined_font
Resume_button.grid(row = 1,column = 3)

# #previous button
# previous_button=Button(root,text="Prev",width =7,command=f.Previous)
# previous_button['font']=defined_font
# previous_button.grid(row=1,column=4)

# #nextbutton
# next_button=Button(root,text="Next",width =7,command=f.Next)
# next_button['font']=defined_font
# next_button.grid(row=1,column=5)

#menu 
menu = Menu(root)
root.config(menu = menu)
add_song_menu=Menu(menu)
# menu.add_cascade(label="Menu",menu=add_song_menu)
# add_song_menu.add_command(label="Add songs",command=f.addsongs)
# add_song_menu.add_command(label="Delete song",command=f.deletesong)


mainloop()
