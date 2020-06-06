from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class Calendario(QWidget):
	def __init__(self, *args, **kwargs):
		super(Calendario, self).__init__(*args, **kwargs)
		self.c = QCalendarWidget()
		layout = QGridLayout(self)
		layout.addWidget(self.c, 0, 0)
		self.setLayout(layout)
		self.dias_da_semana(layout)
		self.meses_do_ano(layout)

	def dias_da_semana(self, layout: QGridLayout):
		dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
		dias = [QLabel(x) for x in dias_semana]
		for x in dias:
			for y in range(7):
				layout.addWidget(x, 1, y)

	def meses_do_ano(self, layout: QGridLayout):
		meses_ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro",
		             "Novembro", "Dezembro"]
		meses = [QLabel(x) for x in meses_ano]
		for x in meses:
			layout.addWidget(x)
