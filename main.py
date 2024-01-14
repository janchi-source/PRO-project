import tkinter as tk
import pygame


a = 1
def on_play_click(event):
    global a
    item = c.find_withtag("current")[0]

    if item == play and a == 1:
        print("play")
        c.itemconfig(item, fill="lime green")
        a = -1
        play_music()
    elif item == play and a == -1:
        print("pause")
        c.itemconfig(item, fill="light grey")
        a = 1
        pygame.mixer.music.pause()

def on_prev_click(event):
    print("previous")

def on_next_click(event):
    print("next")

def on_sound_button_click():
    sound_file = "suka-blyat-made-with-Voicemod-technology.mp3"  
    pygame.mixer.music.load(sound_file)
    print("Sound loaded")

def play_music():
    pygame.mixer.music.play()

def on_search_click():
    search_query = entry_search.get()
    print("Search:", search_query)

root = tk.Tk()

c = tk.Canvas(root, width=800, height=600, background="#191414")
c.pack()

c.create_rectangle(0, 0, 820, 60, fill="grey", outline="black")
c.create_rectangle(0, 540, 820, 610, fill="grey")
play = c.create_oval(375, 545, 425, 595, fill="light grey", width=4, outline="black")
prev_button = c.create_oval(345, 557, 370, 582, fill='light grey', width=3, outline='black')
next_button = c.create_oval(432, 557, 457, 582, fill='light grey', width=3, outline="black")

# Tlačítko pro přehrávání zvuku
sound_button = tk.Button(root, text="Play Sound", command=on_sound_button_click)
sound_button.place(relx=0.5, rely=0.5, anchor="center")

# Vyhledávací pole v levém horním rohu
entry_search = tk.Entry(root, width=20)
entry_search.place(x=10, y=10)

# Nastavení pygame pro přehrávání zvuku
pygame.mixer.init()

c.tag_bind(play, '<ButtonPress-1>', on_play_click)
c.tag_bind(prev_button, '<ButtonPress-1>', on_prev_click)
c.tag_bind(next_button, '<ButtonPress-1>', on_next_click)

# Tlačítko pro spuštění vyhledávání
search_button = tk.Button(root, text="Search", command=on_search_click)
search_button.place(x=150, y=10)

root.mainloop()