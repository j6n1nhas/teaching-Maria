from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *


class Matematica(QWidget):
	def __init__(self, parent=None):
		super(Matematica, self).__init__(parent)
		self.parent = parent
		self.w = W()
		self.setLayout(QGridLayout())
		self.layout().addWidget(self.w, 0, 0)
		self.calculos = CalcArea()
		self.layout().addWidget(self.calculos, 0, 1, 0, 5)
		self.w.plus.clicked.connect(self.winner)

	def winner(self):
		w = Winner(self)
		w.exec()


class W(QWidget):
	def __init__(self):
		super().__init__()
		self.setStyleSheet("background-color: blue; border-color: red; border-width: 5px;")
		self.resize(QSize(100, 200))
		self.image = QLabel()
		canvas = QPixmap("Images/pencil.jpeg")
		self.image.setPixmap(canvas)
		self.plus = QPushButton(QIcon("Icons/plus.png"), "", self)
		self.minus = QPushButton(QIcon("Icons/minus.png"), "", self)
		self.numeros = QPushButton("[1, 2, 3, 4, 5, 6, 7, 8, 9]", self)
		self.setLayout(QVBoxLayout())
		self.layout().addWidget(self.image)
		self.layout().addWidget(self.plus)
		self.layout().addWidget(self.minus)
		self.layout().addWidget(self.numeros)


class CalcArea(QWidget):
	def __init__(self, parent=None):
		super(CalcArea, self).__init__(parent)
		self.setLayout(QGridLayout())
		self.num1 = QLabel("1")
		self.num2 = QLabel("1")
		self.draw = QLabel()
		canvas = QPixmap()
		canvas.fill(Qt.gray)
		self.draw.setPixmap(canvas)
		self.layout().addWidget(self.num1, 0, 0)
		self.layout().addWidget(self.num2, 0, 1)
		self.layout().addWidget(self.draw, 1, 0)


class Winner(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.move(580, 200)
		self.setWindowFlag(Qt.FramelessWindowHint)
		canvas = QPixmap("Images/winner.jpeg")
		self.imagem = QLabel(self)
		self.imagem.setPixmap(canvas)
		self.setFixedSize(canvas.width(), canvas.height())
		self.sound = QSoundEffect()
		self.sound.setSource(QUrl.fromLocalFile("Sounds/Kids_cheering.wav"))
		self.sound.play()
		self.sound.playingChanged.connect(self.close)
