from winsound import PlaySound



songs = []
podcasts = []



class Audio:
    def __init__(self, name, author, path):
        self.name = name
        self.author = author
        self.path = path


    def play(self):
        PlaySound(self.path)


    

class Song(Audio):
    __slots__ = ("name","author","path", "album")

    def __init__(self, name, author, path, album):
        super().__init__(name, author, path)
        self.album = album

        songs.append(self)


    def __repr__(self):
        return f"Song: author {self.author}, album {self.album}, name {self.name}."

    def search_song(self, key):
        found = False
        for song in songs:
            if song.album == key or song.author == key or song.name == key:
                found = True
                return song
        if found == False:
            return f"uups... We don't have that song :("

class Podcast(Audio):
    __slots__ = ("name","author","path", "topic")

    def __init__(self, name, author, path, topic):
        super().__init__(name, author, path)
        self.topic = topic

        podcasts.append(self)

    def __repr__(self):
        return f"Song: author {self.author}, topic {self.topic}, name {self.name}."
    
    def search_podcast(self, key):
        found = False
        for podcast in podcasts:
            if self.topic == key or self.author == key or self.name == key:
                found = True
                return podcast
        if found == False:
            return f"uups... We don't have that podcast :("
        

s1 = Song("Think she was right","Tony Petersen","C:\\Users\\Katarína\\Downloads\\Tony_Petersen_-_Think_She_Was_Right.mp3","idk")
s2 = Song("Happy Mistakes","Azwel","C:\\Users\\Katarína\\Downloads\\Azwel_-_Happy_Mistakes.mp3","idk")
s3 = Song("Burning You",("Tab", "Ron Santee"),"C:\\Users\\Katarína\\Downloads\\Tab_-_Burning_You_(feat.Ron_Santee).mp3","idk")





print(s3.search_song("Happy Mistakes"))