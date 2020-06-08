from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
import sys, string


class Cores(QWidget):
	def __init__(self, *args, **kwargs):
		super(Cores, self).__init__(*args, **kwargs)
		self.cores = {'english': ['blue', 'black', 'white', 'pink', 'green', 'red', 'orange', 'yellow', 'brown', 'grey'],
		              'portugues': ['azul', 'preto', 'branco', 'rosa', 'verde', 'vermelho', 'laranja', 'amarelo', 'castanho', 'cinza'],
		              'castelhano': ['azul', 'negro', 'blanco', 'rosado', 'verde', 'rojo', 'naranja', 'amarillo', 'marrón', 'gris']}
		self.setLayout(QGridLayout())
		"""
		for x in self.cores.values():
			for y in x:
				print(y)
				atual = len(y)
				if atual > maior:
					maior = atual
		print(maior) # maior = 8
		"""
		vlayout = QVBoxLayout()
		hlayout = QHBoxLayout()
		slayout = QStackedLayout()
		self.botoes = dict()
		self.etiquetas = dict()
		self.sound_letters = dict()
		self.build_colors(self.cores['english'])
		self.build_buttons(self.cores['english'], self.layout())
		self.build_slots(slayout)
		self.build_sounds()
		self.intro_sound = QSound("Sounds/Cores_intro.wav", self)
		self.intro_sound.play()

	def build_sounds(self):
		for letter in string.ascii_lowercase:
			self.sound_letters[letter] = QSound("Sounds/Sound_letters/" + letter.upper() + ".wav")
		self.sound_colours = {'english': list(), 'portugues': list(), 'castelhano': list()}
		for lingua, cores in zip(self.sound_colours, self.cores.values()):
			for cor in cores:
				if lingua == 'english':
					self.sound_colours[lingua].append(QSound("Sounds/Idiomas/English/" + cor + ".wav"))
				elif lingua == 'portugues':
					self.sound_colours[lingua].append(QSound("Sounds/Idiomas/Portugues/" + cor + ".wav"))
				else:
					if cor == 'marrón':
						cor = "marron"
					self.sound_colours[lingua].append(QSound("Sounds/Idiomas/Castelhano/" + cor + ".wav"))

	def build_colors(self, cores: list):
		for cor in cores:
			self.etiquetas[cor] = QWidget()
			self.etiquetas[cor].setAutoFillBackground(True)
			palete = self.palette()
			palete.setColor(QPalette.Background, QColor(cor))
			self.etiquetas[cor].setPalette(palete)

	def build_buttons(self, cores: list, layout: QGridLayout):
		self.titulo = QLabel("Clica no botão para conheceres a cor")
		self.titulo.setStyleSheet("font: 32px; color: blue;")
		self.titulo.setAlignment(Qt.AlignCenter)
		palete = self.palette()
		for cor in cores:
			palete.setColor(QPalette.ButtonText, QColor('black'))
			self.botoes[cor] = QPushButton(str(cor).capitalize())
			palete.setColor(QPalette.Button, QColor(cor))
			self.botoes[cor].setPalette(palete)
			if cor == 'black':
				palete.setColor(QPalette.ButtonText, QColor('white'))
				self.botoes[cor].setPalette(palete)
		linha = 1
		coluna = 0
		for botao in self.botoes.values():
			layout.addWidget(botao, linha, coluna, 2, 2)
			coluna += 2
		layout.addWidget(self.titulo, 0, 0, 1, 20)
		layout.addWidget(self.etiquetas['white'], 4, 0, len(self.botoes) * 2, len(self.botoes) * 2)

	def build_slots(self, slayout: QStackedLayout):
		for x, y in self.botoes.items():
			y.clicked.connect(lambda: self.color_clicked(slayout))

	def color_clicked(self, slayout: QStackedLayout):
		if self.intro_sound.isFinished():
			if slayout.parent() == None:
				self.layout().addLayout(slayout, 3, 0, len(self.botoes) * 2, len(self.botoes) * 2)
			if slayout.count() == 0:
				slayout.addWidget(self.etiquetas[str(self.sender().text()).lower()])
				self.escrever_cor(self.sender().text(), slayout)
			else:
				slayout.removeWidget(slayout.currentWidget())
				slayout.addWidget(self.etiquetas[str(self.sender().text()).lower()])
				self.escrever_cor(self.sender().text(), slayout)
			self.dizer_letras(self.sender().text())

	def dizer_letras(self, cor: str):
		index = self.cores['english'].index(cor.lower())
		cor_som_english = list()
		cor_som_portugues = list()
		cor_som_castelhano = list()
		for lingua, palavra in self.cores.items():
			for cor in palavra[index]:
				if lingua == "english":
					cor_som_english.append(self.sound_letters[cor])
				elif lingua == "portugues":
					cor_som_portugues.append(self.sound_letters[cor])
				else:
					if cor == "ó":
						cor = "o"
					cor_som_castelhano.append(self.sound_letters[cor])
		self.sons_gerados = dict()
		self.sons_gerados['english'] = self.gerar_texto(None, cor_som_english)
		self.sons_gerados['portugues'] = self.gerar_texto(None, cor_som_portugues)
		self.sons_gerados['castelhano'] = self.gerar_texto(None, cor_som_castelhano)

	def gerar_texto(self, string: str=None, sons: QSound=None):
		if sons == None:
			for letra in range(1, len(string) + 1):
				yield string[:letra]
		else:
			for som in sons:
				yield som

	def escrever_cor(self, cor: str, slayout: QStackedLayout):
		fonte = QFont("Ubuntu", 32)
		fonte.setLetterSpacing(QFont.AbsoluteSpacing, 42)
		palete = QPalette()
		if cor == "Black":
			palete.setColor(QPalette.WindowText, Qt.white)
		index = self.cores['english'].index(cor.lower())
		palavras = list()
		palavras.append(self.gerar_texto(self.cores['english'][index].capitalize()))
		palavras.append(self.gerar_texto(self.cores['portugues'][index].capitalize()))
		palavras.append(self.gerar_texto(self.cores['castelhano'][index].capitalize()))
		linha = 3
		coluna = 0
		self.labels = list()
		self.timers = [QTimer(), QTimer(), QTimer()]
		for idx, cor in enumerate(palavras):
			self.labels.append(QLabel(slayout.currentWidget()))
			self.labels[idx].setFont(fonte)
			self.labels[idx].setPalette(palete)
			self.layout().addWidget(self.labels[idx], linha, coluna, 1, self.layout().columnCount())
			self.timers[idx].setInterval(1000)
			linha += 1
		self.timers[0].timeout.connect(lambda: self.escrever_ingles(palavras[0]))
		self.timers[1].timeout.connect(lambda: self.escrever_portugues(palavras[1]))
		self.timers[2].timeout.connect(lambda: self.escrever_castelhano(palavras[2]))
		QSound("Sounds/Idiomas/Ingles.wav", self).play()
		self.timers[0].start(2000)

	def escrever_ingles(self, cor: str):
		for l, s in zip(cor, self.sons_gerados['english']):
			self.labels[0].setText("Inglês: " + l)
			s.play()
			return
		self.sender().stop()
		self.dizer_cor(self.labels[0].text().split()[1], 'english')

	def escrever_castelhano(self, cor: str):
		for l, s in zip(cor, self.sons_gerados['castelhano']):
			self.labels[2].setText("Castelhano: " + l)
			s.play()
			return
		self.sender().stop()
		self.dizer_cor(self.labels[2].text().split()[1], 'castelhano')

	def escrever_portugues(self, cor: str):
		for l, s in zip(cor, self.sons_gerados['portugues']):
			self.labels[1].setText("Português: " + l)
			s.play()
			return
		self.sender().stop()
		self.dizer_cor(self.labels[1].text().split()[1], 'portugues')

	def dizer_cor(self, cor: str, lingua: str):
		cor = cor.lower()
		self.next_lingua = None
		if lingua == 'english':
			self.som = QSoundEffect()
			self.som.setSource(QUrl.fromLocalFile("Sounds/Idiomas/English/" + cor + ".wav"))
			self.som.play()
			self.next_lingua = QSoundEffect()
			self.next_lingua.setSource(QUrl.fromLocalFile("Sounds/Idiomas/Portugues.wav"))
			self.next_lingua.playingChanged.connect(lambda: self.timers[1].start(2000))
		elif lingua == 'castelhano':
			self.next_lingua = None
			self.som = QSoundEffect()
			self.som.setSource(QUrl.fromLocalFile("Sounds/Idiomas/Castelhano/" + cor + ".wav"))
		else:
			self.som = QSoundEffect()
			self.som.setSource(QUrl.fromLocalFile("Sounds/Idiomas/Portugues/" + cor + ".wav"))
			self.next_lingua = QSoundEffect()
			self.next_lingua.setSource(QUrl.fromLocalFile("Sounds/Idiomas/Castelhano.wav"))
			self.next_lingua.playingChanged.connect(lambda: self.timers[2].start(2000))
		if self.next_lingua != None:
			self.som.play()
			self.som.playingChanged.connect(self.next_lingua.play)
		else:
			self.som.play()
