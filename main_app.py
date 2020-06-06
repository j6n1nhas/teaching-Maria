from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from calendario import Calendario
from cores import Cores
from matematica import Matematica, Contar


class App(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(App, self).__init__(*args, **kwargs)
		self.setWindowTitle("A Maria a aprender com o pai")
		self.set_toolbar()
		self.set_menus()
		self.setStatusBar(QStatusBar(self))
		self.set_triggers()
		self.showMaximized()

	def set_menus(self):
		menu = QMenuBar()
		self.menus = dict()
		menu_ficheiro = QMenu("Ficheiro", self)
		menu_acoes = QMenu("Ações", self)
		self.menus['sair'] = QAction("Sair", self)
		self.menus['sair'].triggered.connect(self.close)
		menu.addMenu(menu_ficheiro)
		menu.addMenu(menu_acoes)
		for x in self.menus.values():
			menu_ficheiro.addAction(x)
		for x in self.icons.values():
			menu_acoes.addAction(x)
		self.setMenuBar(menu)

	def set_toolbar(self):
		self.icons = dict()
		tbar = QToolBar()
		tbar.setIconSize(QSize(16, 16))
		self.icons['cores'] = QAction(QIcon("Icons/cores.png"), "Cores", self)
		self.icons['cores'].setStatusTip("O pai vai ensinar as cores à Maria")
		self.icons['calculadora'] = QAction(QIcon("Icons/calculadora.png"), "Calculadora", self)
		self.icons['calculadora'].setStatusTip("O pai vai ensinar os números à Maria")
		self.icons['calendario'] = QAction(QIcon("Icons/calendario.png"), "Calendário", self)
		self.icons['calendario'].setStatusTip("O pai vai ensinar os dias à Maria")
		self.icons['culinaria'] = QAction(QIcon("Icons/culinaria.png"), "Culinária", self)
		self.icons['culinaria'].setStatusTip("Será que a Maria ainda se lembra das receitas que a mãe ensinou?")
		for x in self.icons.values():
			tbar.addAction(x)
		tbar.setContextMenuPolicy(Qt.PreventContextMenu)  # Esta linha previne que o utilizador consiga remover a toolbar
		self.addToolBar(tbar)

	def set_triggers(self):
		self.icons['calendario'].triggered.connect(self.tarefa_calendario)
		self.icons['cores'].triggered.connect(self.tarefa_cores)
		self.icons['calculadora'].triggered.connect(self.tarefa_calculadora)

	def tarefa_calculadora(self):
		self.calc = Matematica()
		self.setCentralWidget(self.calc)

	def tarefa_calendario(self):
		self.c = Calendario()
		self.setCentralWidget(self.c)

	def tarefa_cores(self):
		self.cor = Cores()
		self.setCentralWidget(self.cor)

raiz = QApplication(sys.argv)
app = App()
raiz.exec_()