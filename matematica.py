from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class Contar(QThread):
	def __init__(self, range=None, lingua=None, parent=None):
		super(Contar, self).__init__(parent)
		self.range = range
		self.lingua = lingua

	def run(self):
		for numero in range(self.range):
			print(str(numero))
			self.sleep(0.5)


class Matematica(QWidget):
	def __init__(self, *args, **kwargs):
		super(Matematica, self).__init__(*args, **kwargs)
		self.setLayout(QGridLayout())
		self.label = QLabel(self)
		self.layout().addWidget(self.label, 0, 0)
		t = Contar(range=10)
		t.start()
		#self.label.setText(t.start())
