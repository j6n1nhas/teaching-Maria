from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys, time
from temp2 import Cor

# !/usr/bin/env python

import os
import sys

class BasicWindow(QMainWindow):

	def __init__(self, parent=None):
		super(BasicWindow, self).__init__(parent)

		# self.setupUi(self)
		self.label = QLabel(self)
		self.label.setGeometry(QRect(73, 110, 574, 331))
		self.pushButton = QPushButton(self)
		self.pushButton.setGeometry(QRect(66, 30, 75, 27))
		self.pushButton.setText("DoIt")

		scrX = 2048
		scrY = 1150
		winX = 720
		winY = 530
		pX = (scrX - winX) / 2
		pY = (scrY - winY) / 2

		self.setGeometry(pX, pY, winX, winY)

		self.label.setText('')
		self.pushButton.clicked.connect(self.DoIt)
		self.timer = QTimer(interval=300, timeout=self.timeout)

	def DoIt(self):
		self.textGen = self.generateText()
		self.timer.start()

	def generateText(self):
		text = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna"

		for i in range(len(text)):
			yield text[:i]

	def timeout(self):
		for accum in self.textGen:
			self.label.setText(accum)
			print(accum)
			return
		self.timer.stop()


def main():
	app = QApplication(sys.argv)
	form = BasicWindow()
	form.show()
	app.exec_()


if __name__ == '__main__':
	main()

