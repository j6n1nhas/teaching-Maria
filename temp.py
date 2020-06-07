from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
import sys, time, traceback


class Thread(QThread):
	valor = pyqtSignal(int)

	def run(self):
		contagem = 0
		while contagem <= 100:
			contagem += 1
			self.sleep(1)
			self.valor.emit(contagem)


class MainWindow(QDialog):
	def __init__(self):
		super().__init__()
		self.title = "PyQt5 ProgressBar"
		self.top = 200
		self.left = 500
		self.width = 300
		self.height = 100
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		vbox = QVBoxLayout()
		self.progressbar = QProgressBar()
		# self.progressbar.setOrientation(Qt.Vertical)
		self.progressbar.setMaximum(100)
		self.progressbar.setStyleSheet("QProgressBar {border: 2px solid grey;border-radius:8px;padding:1px}"
		                               "QProgressBar::chunk {background:yellow}")
		# qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 red, stop: 1 white);
		# self.progressbar.setStyleSheet("QProgressBar::chunk {background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 red, stop: 1 white); }")
		# self.progressbar.setTextVisible(False)
		vbox.addWidget(self.progressbar)
		self.button = QPushButton("Start Progressbar")
		self.button.clicked.connect(self.startProgressBar)
		self.button.setStyleSheet('background-color:yellow')
		vbox.addWidget(self.button)
		self.setLayout(vbox)
		self.show()

	def startProgressBar(self):
		self.thread = Thread()
		self.thread.valor.connect(self.mostrar_progresso)
		self.thread.start()

	def mostrar_progresso(self, valor):
		self.progressbar.setValue(valor)


if __name__ == '__main__':
	raiz = QApplication(sys.argv)
	app = MainWindow()
	raiz.exec_()
	print("Terminado")