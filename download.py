from pytube import YouTube
from PyQt5.QtWidgets import QMessageBox

def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        mp4_filename = f'{yt.title}.mp4'
        stream.download(output_path = './', filename = mp4_filename)
        show_popup(mp4_filename)

    except Exception as e:
        print(f'Error : {e}')

def download_mp3(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio = True).first()
        mp3_filename = f'{yt.title}.mp3'
        stream.download(output_path = './', filename = mp3_filename)
        show_popup(mp3_filename)

    except Exception as e:
        print(f'Error: {e}')

def show_popup(video_title):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("Download Completed Successfully!")
    msg.setText(f"{video_title} File Downloaded Successfully.")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()
