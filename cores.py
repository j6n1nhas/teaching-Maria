from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
import sys, string


class Cores(QWidget):
	def __init__(self, *args, **kwargs):
		super(Cores, self).__init__(*args, **kwargs)

		"""
		self.cores: variável dict com a seguinte estrutura:
		keys: idiomas
		values: variável list com a representação string de cada cor
		"""
		self.cores = {'english': ['blue', 'black', 'white', 'pink', 'green', 'red', 'orange', 'yellow', 'brown', 'grey'],
		              'portugues': ['azul', 'preto', 'branco', 'rosa', 'verde', 'vermelho', 'laranja', 'amarelo', 'castanho', 'cinza'],
		              'castelhano': ['azul', 'negro', 'blanco', 'rosado', 'verde', 'rojo', 'naranja', 'amarillo', 'marrón', 'gris']}

		# Criação e definição de layout a utilizar no módulo
		vlayout = QVBoxLayout()
		hlayout = QHBoxLayout()
		self.slayout = QStackedLayout()
		self.setLayout(QGridLayout())

		self.botoes = self.build_buttons(self.cores['english'])
		self.etiquetas = self.build_colors(self.cores['english'])
		self.sound_letters, self.sound_lang, self.sound_colors = self.build_sounds()
		self.layingout(self.layout())
		self.build_slots()
		self.intro_sound = QSound("Sounds/Cores_intro.wav", self)
		self.intro_sound.play()

		"""
		for x in self.cores.values():
			for y in x:
				print(y)
				atual = len(y)
				if atual > maior:
					maior = atual
		print(maior) # maior = 8
		"""

	def layingout(self, layout: QGridLayout):
		"""
		Método para dispor os widgets no monitor utilizando o QGridLayout da aplicação
		:param layout: QGridLayout definido para a aplicação e obtido com self.layout()
		:return: None
		"""
		self.velocidade = QSlider(Qt.Horizontal)
		self.velocidade.setRange(1, 10)
		self.velocidade.setSingleStep(1)
		self.velocidade.setPageStep(2)
		self.velocidade.setTickPosition(QSlider.TicksBelow)
		self.velocidade.setTickInterval(1)
		self.velocidade.setFixedWidth(200)
		self.velocidade.setValue(4)
		self.titulo = QLabel("Clica no botão para conheceres a cor")
		self.titulo.setStyleSheet("font: 32px; color: blue;")
		self.titulo.setAlignment(Qt.AlignCenter)
		linha = 1
		coluna = 0
		for botao in self.botoes.values():
			layout.addWidget(botao, linha, coluna, 2, 2)
			coluna += 2
		layout.addWidget(self.titulo, 0, 0, 1, 20)
		layout.addWidget(QLabel("Velocidade"), 0, 15)
		layout.addWidget(self.velocidade, 0, 16, 2, 4)
		layout.addLayout(self.slayout, 3, 0, len(self.botoes) * 2, len(self.botoes) * 2)
		for cor in self.etiquetas.values():
			self.slayout.addWidget(cor)
		self.slayout.setCurrentIndex(2)

	def build_buttons(self, cores: list):
		"""
		Cria um botão para cada cor na variável self.botoes e dispõe-nos no layout do widget
		:param cores: list com as cores em inglês
		:return: botoes -> self.botoes (dict()): Contém nas keys as cores em inglês e nos values, os QPushButton
		"""
		botoes = dict()
		palete = self.palette()
		for cor in cores:
			palete.setColor(QPalette.ButtonText, QColor('black'))
			botoes[cor] = QPushButton(str(cor).capitalize())
			palete.setColor(QPalette.Button, QColor(cor))
			if cor == 'black':
				palete.setColor(QPalette.ButtonText, QColor('white'))
			botoes[cor].setPalette(palete)
		return botoes

	def build_colors(self, cores: list):
		"""
		Define um widget para cada cor dentro da variável self.etiquetas
		:param cores: list com as cores em inglês
		:return: self.etiquetas (dict()): Contém nas chaves as cores em inglês e nos values, os QWidget de cada cor
		"""
		etiquetas = dict()
		for cor in cores:
			etiquetas[cor] = QWidget()
			etiquetas[cor].setAutoFillBackground(True)
			palete = self.palette()
			palete.setColor(QPalette.Background, QColor(cor))
			etiquetas[cor].setPalette(palete)
		return etiquetas

	def build_sounds(self):
		"""
		Método que cria e devolve as variáveis de tipo dict() relacionados com sons:
		:return: letters -> self.sound_letters / idiomas -> self.sound_lang / cores -> self.sound_colors
		"""
		abc = string.ascii_lowercase
		letters = dict.fromkeys(abc)
		idiomas = dict.fromkeys(self.cores)
		cores = dict.fromkeys(self.cores)
		for key, value in cores.items():
			cores[key] = list()

		# Criação do dicionário que contém os sons de cada letra
		for letra in letters:
			letters[letra] = QSoundEffect(self)
			letters[letra].setSource(QUrl.fromLocalFile("Sounds/Sound_letters/" + letra + ".wav"))

		# Criação do dicionário que contém os sons das cores em cada língua
		for key, value in self.cores.items():
			for item in value:
				som = QSoundEffect(self)
				if key == 'english':
					som.setSource(QUrl.fromLocalFile("Sounds/Idiomas/English/" + item + ".wav"))
					cores[key].append(som)
				elif key == 'portugues':
					som.setSource(QUrl.fromLocalFile("Sounds/Idiomas/Portugues/" + item + ".wav"))
					cores[key].append(som)
				else:
					if item == 'marrón':
						item = 'marron'
					som.setSource(QUrl.fromLocalFile("Sounds/Idiomas/Castelhano/" + item + ".wav"))
					cores[key].append(som)

		# Criação do dicionário que contém os sons de cada idioma
		idiomas['english'] = QSoundEffect(self)
		idiomas['english'].setSource(QUrl.fromLocalFile("Sounds/Idiomas/Ingles.wav"))
		idiomas['portugues'] = QSoundEffect(self)
		idiomas['portugues'].setSource(QUrl.fromLocalFile("Sounds/Idiomas/Portugues.wav"))
		idiomas['castelhano'] = QSoundEffect(self)
		idiomas['castelhano'].setSource(QUrl.fromLocalFile("Sounds/Idiomas/Castelhano.wav"))
		return letters, idiomas, cores

	def build_slots(self):
		"""
		Método para ligar os widgets às ações
		:return: None
		"""
		for botao in self.botoes.values():
			botao.clicked.connect(self.color_clicked)
		self.velocidade.valueChanged.connect(self.mudar_velocidade)

	def mudar_velocidade(self):
		velocidade = self.velocidade.value() * 500
		for x in self.timers:
			x.setInterval(velocidade)

	def color_clicked(self):
		cor = self.sender().text().lower()
		items = list(self.botoes.keys())
		idx = items.index(cor)
		if self.intro_sound.isFinished():
			fonte = QFont("Ubuntu", 32)
			fonte.setLetterSpacing(QFont.AbsoluteSpacing, 42)
			palete = QPalette()
			if self.cores['english'][idx] == "black":
				palete.setColor(QPalette.WindowText, Qt.white)
			self.slayout.setCurrentIndex(idx)
			linha = 3
			coluna = 0
			self.labels = list()
			self.timers = [QTimer(), QTimer(), QTimer()]
			for i in range(3):
				self.labels.append(QLabel())
				self.labels[i].setFont(fonte)
				self.labels[i].setPalette(palete)
				self.layout().addWidget(self.labels[i], linha, coluna, 2, self.layout().columnCount())
				self.timers[i].setInterval(self.velocidade.value() * 500)
				linha += 3
			self.dizer_letras(cor)
			palavras = list()
			palavras.append(self.gerador(self.cores['english'][idx].capitalize()))
			palavras.append(self.gerador(self.cores['portugues'][idx].capitalize()))
			palavras.append(self.gerador(self.cores['castelhano'][idx].capitalize()))
			self.timers[0].timeout.connect(lambda: self.escrever_ingles(palavras[0]))
			self.timers[1].timeout.connect(lambda: self.escrever_portugues(palavras[1]))
			self.timers[2].timeout.connect(lambda: self.escrever_castelhano(palavras[2]))
			QSound("Sounds/Idiomas/Ingles.wav", self).play()
			self.timers[0].start(2000)

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
		self.sons_gerados['english'] = self.gerador(None, cor_som_english)
		self.sons_gerados['portugues'] = self.gerador(None, cor_som_portugues)
		self.sons_gerados['castelhano'] = self.gerador(None, cor_som_castelhano)

	def gerador(self, string: str = None, sons: QSoundEffect = None):
		if sons == None:
			for letra in range(1, len(string) + 1):
				yield string[:letra]
		else:
			for som in sons:
				yield som

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
			self.som.playingChanged.connect(self.next_lingua.play)
			self.next_lingua.playingChanged.connect(self.timers[1].start)
		elif lingua == 'castelhano':
			if cor == 'marrón':
				cor = 'marron'
			self.next_lingua = None
			self.som = QSoundEffect()
			self.som.setSource(QUrl.fromLocalFile("Sounds/Idiomas/Castelhano/" + cor + ".wav"))
			self.som.play()
		else:
			self.som = QSoundEffect()
			self.som.setSource(QUrl.fromLocalFile("Sounds/Idiomas/Portugues/" + cor + ".wav"))
			self.som.play()
			self.next_lingua = QSoundEffect()
			self.next_lingua.setSource(QUrl.fromLocalFile("Sounds/Idiomas/Castelhano.wav"))
			self.som.playingChanged.connect(self.next_lingua.play)
			self.next_lingua.playingChanged.connect(self.timers[2].start)
