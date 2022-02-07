import sys
from SpotyUNIF import *
from PySide2 import QtCore
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QPropertyAnimation # paquete necesario para crear el menu lateral desplegable
from PySide2 import QtCore, QtGui, QtWidgets
from pygame import mixer



class SpotyUNI(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow() 
		self.ui.setupUi(self)

		#eliminar barra y de titulo - opacidad
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setWindowOpacity(1)

		#SizeGrip
		self.gripSize = 10
		self.grip = QtWidgets.QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)

		# mover ventana
		self.ui.frame_superior.mouseMoveEvent = self.mover_ventana

		#acceder a las paginas
		self.ui.bt_inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_inicio))			
		self.ui.bt_canciones.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
		self.ui.bt_planes.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))	
		self.ui.bt_cliente.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
		self.ui.bt_pp_cliente.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))			
		self.ui.bt_listas.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))	

		#control barra de titulos
		self.ui.bt_ocultar.clicked.connect(self.control_bt_ocultar)		
		self.ui.bt_minimizar.clicked.connect(self.control_bt_normal)
		self.ui.bt_maximizar.clicked.connect(self.control_bt_maximizar)
		self.ui.bt_cerrar.clicked.connect(lambda: self.close())

		#control barra de reprodcucción
		# self.ui.bt_canciones_2.cliked.connect(self.no_exite)
		self.ui.bt_reproducir.clicked.connect(self.control_bt_reproducir)		
		self.ui.bt_pausar.clicked.connect(self.control_bt_pausar)
		self.ui.bt_reanudar.clicked.connect(self.control_bt_reanudar)
		self.ui.bt_detener.clicked.connect(self.control_bt_detener)
		self.ui.volumen.valueChanged.connect(self.control_volumen)
		

		self.ui.bt_ocultar.hide()

		#menu lateral
		self.ui.bt_menu.clicked.connect(self.mover_menu)

	def control_bt_reproducir(self):
		mixer.init()
		mixer.music.load("C:\SpotyUN\Canciones//never_gonna_give_you_up.mp3")
		mixer.music.play()

	def control_bt_pausar(self):
		mixer.music.pause()

	def control_bt_reanudar(self):
		mixer.music.unpause()

	def control_bt_detener(self):
		mixer.music.stop()


	def control_volumen(self):
		value = self.ui.volumen.value()
		mixer.music.set_volume(value/100)	


	# -------------------------------------------------------------

	def control_bt_ocultar(self):
		self.showMinimized()		

	def  control_bt_normal(self): 
		self.showNormal()		
		self.ui.bt_ocultar.hide()
		self.ui.bt_maximizar.show()

	def  control_bt_maximizar(self): 
		self.showMaximized()
		self.ui.bt_maximizar.hide()
		self.ui.bt_ocultar.show()

	def mover_menu(self):
		if True:			
			width = self.ui.frame_lateral.width()
			normal = 0
			if width==0:
				extender = 250
			else:
				extender = normal
			self.animacion = QPropertyAnimation(self.ui.frame_lateral, b'minimumWidth')
			self.animacion.setDuration(300)
			self.animacion.setStartValue(width)
			self.animacion.setEndValue(extender)
			self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
			self.animacion.start()

	## SizeGrip
	def resizeEvent(self, event):
		rect = self.rect()
		self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

	## mover ventana
	def mousePressEvent(self, event):
		self.clickPosition = event.globalPos()

	def mover_ventana(self, event):
		if self.isMaximized() == False:			
			if event.buttons() == Qt.LeftButton:
				self.move(self.pos() + event.globalPos() - self.clickPosition)
				self.clickPosition = event.globalPos()
				event.accept()

		if event.globalPos().y() <=20:
			self.showMaximized()
		else:
			self.showNormal()


if __name__ == "__main__":
     program = QApplication(sys.argv)
     my_program = SpotyUNI()
     my_program.show()
     sys.exit(program.exec_())	
