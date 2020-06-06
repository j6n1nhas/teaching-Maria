from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys, random, time


class Cor(QWidget):
	def __init__(self, cor, *args, **kwargs):
		super(Cor, self).__init__(*args, **kwargs)
		self.setAutoFillBackground(True)
		palete = self.palette()
		palete.setColor(QPalette.Window, QColor(cor))
		self.setPalette(palete)


class App(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(App, self).__init__(*args, **kwargs)
		self.setWindowTitle("A minha app")
		cores = QColor().colorNames()
		layout = QVBoxLayout()
		intervalo = 50
		# self.solo_widget(cores, layout)
		self.varios_widgets(cores, layout, intervalo)
		self.showMaximized()

	def varios_widgets(self, cores, layout, intervalo):
		self.widgets_cores = [Cor(x) for x in cores[intervalo::2]]
		zipper = zip(self.widgets_cores, cores[:intervalo])
		self.widgets_etiquetas = [QLabel("A presente cor é: " + x, y) for y, x in zipper]
		font = QFont("Ubuntu")
		font.setPointSize(5)
		for x in self.widgets_etiquetas:
			x.setFont(font)
		self.main = QWidget()
		for x in self.widgets_cores:
			layout.addWidget(x)
		self.main.setLayout(layout)
		self.setCentralWidget(self.main)

	def solo_widget(self, cores, layout):
		self.main = QWidget()
		self.main.setLayout(layout)
		cor = random.choice(cores)
		self.widget = Cor(cor)
		etiqueta = QLabel("A cor escolhida é: " + cor, self.widget)
		etiqueta.setAlignment(Qt.AlignCenter)
		layout.addWidget(self.widget)
		self.setCentralWidget(self.main)


if __name__ == '__main__':
	root = QApplication([])
	app = App()
	root.exec_()