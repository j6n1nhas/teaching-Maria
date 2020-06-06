from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
import sys, time, traceback


class Obj(QObject):
	"""
	Criação de sinais disponíveis para uma tarefa em thread:
	terminado: sinal enviado sem mais informação, quando o processamento terminar
	erro: tuple com informação sobre um eventual erro que possa surgir
	resultado: qualquer coisa que resulte do processamento.
	"""
	terminado = pyqtSignal()
	erro = pyqtSignal(tuple)
	resultado = pyqtSignal(object)


class Tarefa(QRunnable):
	def __init__(self, fn, *args, **kwargs):
		super(Tarefa, self).__init__(*args, **kwargs)
		self.fn = fn
		self.args = args
		self.kwargs = kwargs
		self.sinais = Obj()

	@pyqtSlot()
	def run(self):
		try:
			resultado = self.fn(self.args, self.kwargs)
		except:
			traceback.print_exc()
			tipo, valor = sys.exc_info()[:2]
			self.sinais.erro.emit((tipo, valor, traceback.format_exc()))
		else:
			self.sinais.resultado.emit(resultado)
		finally:
			self.sinais.terminado.emit()


if __name__ == '__main__':
	raiz = QApplication(sys.argv)
	app = MainWindow()
	raiz.exec_()
	print("Terminado")