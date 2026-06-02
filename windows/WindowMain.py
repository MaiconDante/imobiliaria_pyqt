from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton
)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        # Define o título da janela
        self.setWindowTitle("Sistema de Cadastro de Imóveis da Imobiliária")
        # Define (Largura x Altura) da janela
        self.resize(800, 600)
        # Cria um organizador vertical
        layout = QVBoxLayout()
        # [LABELS] Texto que será exibido dentro da janela - [CRIA O COMPONENTE]
        titulo = QLabel("Cadastro de Imóveis")
        label_codigo = QLabel("Código do Imóvel")
        label_endereco = QLabel("Endereço do Imóvel")
        label_cidade = QLabel("Cidade do Imóvel")
        informacao = QLabel("Sistema desenvolvido em PyQt6")
        versao = QLabel("Versão 1.0")
        # [INPUTS] Campos de texto para usuário digitar, que será exibido dentro da janela - [CRIA O COMPONENTE]
        self.input_codigo = QLineEdit()
        self.input_codigo.setPlaceholderText("Digite o código do Imóvel")
        self.input_endereco = QLineEdit()
        self.input_endereco.setPlaceholderText("Digite o endereço do Imóvel")
        self.input_cidade = QLineEdit()
        self.input_cidade.setPlaceholderText("Digite a cidade do Imóvel")
        # [BUTTONS] Botões de ação
        btn_salvar = QPushButton("Salvar Imóvel")
        btn_salvar.clicked.connect(self.salvar_imovel)
        # Adiciona o texto na janela - [COLOCA O COMPONENTE NA TELA]
        layout.addWidget(titulo)
        layout.addWidget(label_codigo)
        layout.addWidget(self.input_codigo)
        layout.addWidget(label_endereco)
        layout.addWidget(self.input_endereco)
        layout.addWidget(label_cidade)
        layout.addWidget(self.input_cidade)
        layout.addWidget(informacao)
        layout.addWidget(versao)
        layout.addWidget(btn_salvar)
        # Aqui diz esta janela usará este layout
        self.setLayout(layout)

    def salvar_imovel(self):
        texto_atual = self.windowTitle()

        if texto_atual == "Sistema de Cadastro de Imóveis da Imobiliária":
            self.setWindowTitle("Clique Detectado")
        else:
            self.setWindowTitle("Sistema de Cadastro de Imóveis da Imobiliária")