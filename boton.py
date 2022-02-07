class Mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.reproducir.clicked.connect(self.btnReproducir)
        self.ui.parar.clicked.connect(self.btnParar)
        self.ui.reanudar.clicked.connect(self.btnReanudar)
        self.ui.salir.clicked.connect(self.btnSalir)
        print(self.ui.verticalSlider.valueChanged.connect(self.verticalSlider))
        # conecte la señal del clicked signal el slot btnClicked
    def btnReproducir(self):
        print('boton Reproducir')
        mixer.init()
        mixer.music.load("C:\\Users\\AMD\\Documents\\Programs\\Python\\Universidad\\SpotyUN\\Canciones\\ordinary_people.mp3")
        mixer.music.play()
    def btnParar(self):
        print('boton Parar')
        mixer.music.pause()
    def btnReanudar(self):
        print('boton Reanudar')
        mixer.music.unpause()
    def btnSalir(self):
        print('boton Ssalir')
        mixer.music.stop()

    def verticalSlider(self):
        value = self.ui.verticalSlider.value()
        mixer.music.set_volume(value/100)
app = QtWidgets.QApplication([])
application = Mywindow()
application.show()
sys.exit(app.exec()


"""

import os
import sys

from PyQt5 import QtCore, QtMultimedia

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def main():
    filename = os.path.join(CURRENT_DIR, "sound.mp3")

    app = QtCore.QCoreApplication(sys.argv)

    player = QtMultimedia.QMediaPlayer()

    def handle_state_changed(state):
        if state == QtMultimedia.QMediaPlayer.PlayingState:
            print("started")
        elif state == QtMultimedia.QMediaPlayer.StoppedState:
            print("finished")
            QtCore.QCoreApplication.quit()

    player.stateChanged.connect(handle_state_changed)

    url = QtCore.QUrl.fromLocalFile(filename)
    player.setMedia(QtMultimedia.QMediaContent(url))
    player.play()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()"""