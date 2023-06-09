from PyQt5 import QtWidgets
import sys
from Download import YoutubeDownloader
from YoutubeConverter import Ui_MainWindow

class App(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_mp3.clicked.connect(self.download)
        self.ui.btn_mp4.clicked.connect(self.download)

    def download(self):
        sender = self.sender().text()
        url = self.ui.txt_url.text()
        downloader = YoutubeDownloader()
        
        if sender == 'MP3':
            downloader.download_mp3(url)
            
        elif sender == 'MP4':
            downloader.download_video(url)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = App()

    win.show()
    sys.exit(app.exec_())
