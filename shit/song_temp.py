from audio import Audio

class Song(Audio):
    def __init__(self, publisher, date, duration, path):
        super().__init__(publisher, date, duration)
        self.path = path

        self.autor = publisher
        self.duration = duration
        self.date = date
        self.extract_data()

    def extract_data(self):
        temp_list = self.path.split('/')
        temp = temp_list[2].split('.')
        temp_f = temp[0]
        with open(f"database/{temp_f}.txt", "r") as temp_read:
            temp_list2 = temp_read.readlines()
            self.album = temp_list2[3].split(';')[1].split('\n')[0]

        print(self.album)


s = Song(path = "database/aaac.txt")
