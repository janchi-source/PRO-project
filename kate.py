import os
from audio import *
import tkinter as tk

# its object is something like a list of albums and its interprets(so u need only one for the whole project)
class Albums(Audio):
    def __init__(self):
        self.albums = []

#creating album (a text document named by publisher placed in database based on a system album;abcd.txt)
#I made it like this so we wont have that much text document as we would had its own file
    def create_album(self):
#takes all the paths of files in the database
        data_files = os.listdir("database")
        dir_list = []

#here I will append every text song file to the list(and make shure that it wont take the paths document or the .mp3 document)
        for file in data_files:
            if (".txt" in file) and (file != "paths.txt") and "_albums" not in file:
                dir_list.append(file)

#make sure that this album doesnt exist(so we wont have it there twice)  
        for file in dir_list:
            with open(f"database/{file}", "r") as f:
                for line in f:
                    if "publisher;" in line:
                        publisher_list = line.split(";")[1].split("\n")
                        publisher = publisher_list[0]

                    if "album;" in line:
                        album_list = line.split(";")[1].split("\n")
                        album = album_list[0]

                existing_album = False
                for ithem in self.albums:
                    if f"{publisher},{album}" == ithem:
                        existing_album = True

#creates album if it is needed
                if existing_album == False:
                    with open(f"database/{publisher}_albums.txt","w") as f:
                        f.write(f"{album};{file};\n")
                        self.albums.append(f"{publisher},{album}")

#if the album exists but the song isnt there, we will add it
                else:
                    self.add_song_to_album(album,publisher, file)



    def add_song_to_album(self, album, publisher, name_of_text_file_of_song):
        inalbum = False
        searching = True
        firstLines = ""
        lastLines = ""

#checks if the album exists (if not it will create it)
        if f"{publisher},{album}" not in self.albums:
            print ("Error:This album does not exist. You cant use add_song_to_album().")
            self.create_album()

#adding the song
        with open(f"database/{publisher}_albums.txt","r") as f:
            global added
            for line in f:
                if searching:
                    if album in line:
                        line_list = line.split(";")
                        if name_of_text_file_of_song in line_list[1]:
                            print ("Error: this song is already in the album.")
                            inalbum = True
                        
                        elif line_list[0] == album:
                            added = line.replace (line_list[1], (line_list[1] + f",{name_of_text_file_of_song}"))
                            searching = False
                            

                    else:
                        firstLines += line
                else:
                    lastLines += line

        if inalbum == False:
            print (inalbum)
            with open(f"database/{publisher}_albums.txt","w") as f:
                f.write (firstLines)
                f.write (added)
                f.write (lastLines)

 #here I havent used the click event but I made it react on the input (so basically it will react with any event)
    def draw_album(self):
        c = tk.Canvas(width=1000,height=1000, background="violet")
        c.pack()

        width = 200
        height = 80
        x, y = 50,50
        album_btn = []

#drawing albums
        for album in self.albums:
            if x<=1000:
                b = c.create_rectangle(x,y,x+width, y+height, fill="limegreen")
                t = c.create_text(x+100,y+40,text=f"{album}")
                x += 250
                album_btn.append(b)
                album_btn.append(t)
            else:
                y += 130
                c.create_rectangle(x,y,x+width, y+height, fill="limegreen")
                c.create_text(x+100,y+40,text=f"{album}")
                x += 250
                album_btn.append(b)
                album_btn.append(t)

#my 'event'
            inp = input("Songs:")

        if inp == ".":
            for btn in album_btn:
                c.delete(btn)

#ready for the 'if event.click == on that button -> chosen_publisher will be "Tublatanka" and chosen_album will be "Skusime to cez vesmir" '
#takes all the names of text files of the songs in the album
            chosen_publisher = "Tublatanka"
            chosen_album = "Skusime to cez vesmir"
            with open(f"database/{chosen_publisher}_albums.txt", "r") as f:
                for line in f:
                    ll = line.split(";")
                    # print (ll)
                    # print (ll[1])
                    if ll[0] == chosen_album:
                        songs = ll[1].split(",")
                        # print (songs)

#find the actual names of the songs
            names_of_songs_in_album = []
            for song in songs:
                with open(f"database/{song}") as file:
                    for line in file:
                        if "name" in line:
                            name = line.split(";")[1].split("\n")
                            song_name = name[0]
                            names_of_songs_in_album.append(song_name)  #cannot use diacritics in the names of the songs

#draw the buttons with the names of songs on it
            width = 200
            height = 80
            x, y = 50,50
            song_btn = []
                
            for s in names_of_songs_in_album:
                if x<=1000:
                    b = c.create_rectangle(x,y,x+width, y+height, fill="limegreen")
                    t = c.create_text(x+100,y+40,text=f"{s}")
                    x += 250
                    song_btn.append(b)
                    song_btn.append(t)
                else:
                    y += 130
                    c.create_rectangle(x,y,x+width, y+height, fill="limegreen")
                    c.create_text(x+100,y+40,text=f"{s}")
                    x += 250
                    song_btn.append(b)
                    song_btn.append(t)

        c.mainloop()

##all you need to use this album 
# spotify = Albums()
# spotify.create_album()
# spotify.draw_album()

###PLEASE DONT USE THE DIACRITICS IN THE NAMES OF THE SONGS

