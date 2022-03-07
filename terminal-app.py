
from pytube import YouTube


save_path = '/Downloads'

videoUrl = input('Digite a URL de um vídeo: ')

video = YouTube(videoUrl)

videofile = video.streams.get_highest_resolution()

videofile.download(save_path)

print(video.title + ' foi baixando e se encontra em: ' + save_path)