
class Audio:
    def __init__(self, song_path):
        global temp_f
        self.song_path = song_path
        self.extract_data()

    def extract_data(self):
        temp_list = self.song_path.split('/')
        temp = temp_list[2].split('.')
        temp_f = temp[0]

        

        with open(f"database/{temp_f}.txt", "r") as temp_read:
            self.publisher = temp_read.readline().split(';')[1].split('\n')[0]
            self.title = temp_read.readline().split(';')[1].split('\n')[0]
            self.date = temp_read.readline().split(';')[1].split('\n')[0]
            self.duration = temp_read.readline().split(';')[1].split('\n')[0]

        self.name = self.publisher + " - " + self.title

    def get_path(self):
        return self.song_path.split('/')[1] + "/" + self.song_path.split('/')[2]
            
        # def album_list(self):
        #     self.album_stack = []
        #     if self.album in self.stack == False:
        #         self.album_stack.append(self.album)


