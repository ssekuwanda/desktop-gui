import eel
from pytube import YouTube
eel.init('web')

@eel.expose
def download_video(url):
    link = str(url)
    YouTube(link).streams.first().download()
    return 'finished downloading'

@eel.expose
def download_audio(url):
    link = str(url)
    yt = YouTube(link)
    dl = yt.streams.filter(only_audio=True).all()
    dl[0].download()
    return 'finished downloading audio'

eel.start('main.html')

# https://www.youtube.com/watch?v=B7bqAsxee4I