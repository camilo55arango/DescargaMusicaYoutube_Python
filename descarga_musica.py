import pytube
from pytube import YouTube
from moviepy.editor import *

def descargar_musica(url):
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()

    # Descarga el archivo de audio y lo guarda en formato MP3
    audio.download()
    mp4_file = audio.default_filename
    mp3_file = mp4_file.replace(".mp4", ".mp3")
    video = AudioFileClip(mp4_file)
    video.write_audiofile(mp3_file)
    video.close()

def main():
    url = input("Ingresa la URL del video de YouTube: ")
    descargar_musica(url)
    print("La música se ha descargado exitosamente.")
    
main()
