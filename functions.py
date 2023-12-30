import winsound as ws

def play(path):
    ws.PlaySound(path, ws.SND_FILENAME)