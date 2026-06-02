from PyQt6.QtWidgets import (
    QWidget,
    QFormLayout,
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
        layout = QFormLayout()
        # [LABELS] Texto que será exibido dentro da janela - [CRIA O COMPONENTE]
        titulo = QLabel("Cadastro de Imóveis")
        informacao = QLabel("Sistema desenvolvido em PyQt6")
        versao = QLabel("Versão 1.0")
        # [INPUTS] Campos de texto para usuário digitar, que será exibido dentro da janela - [CRIA O COMPONENTE]
        self.input_codigo = QLineEdit()
        self.input_codigo.setPlaceholderText("Digite o código do Imóvel")
        self.input_endereco = QLineEdit()
        self.input_endereco.setPlaceholderText("Digite o endereço do Imóvel")
        self.input_bairro = QLineEdit()
        self.input_bairro.setPlaceholderText("Digite o bairro do Imóvel")
        self.input_cidade = QLineEdit()
        self.input_cidade.setPlaceholderText("Digite a cidade do Imóvel")
        # [BUTTONS] Botões de ação
        btn_salvar = QPushButton("Salvar Imóvel")
        btn_salvar.clicked.connect(self.salvar_imovel)
        # Adiciona o texto na janela - [COLOCA O COMPONENTE NA TELA]
        layout.addRow(titulo)
        layout.addRow(
            "Código do Imóvel:",
            self.input_codigo
        )

        layout.addRow(
            "Endereço do Imóvel:",
            self.input_endereco
        )

        layout.addRow(
            "Bairro do Imóvel:",
            self.input_bairro
        )

        layout.addRow(
            "Cidade do Imóvel:",
            self.input_cidade
        )
        layout.addRow(informacao)
        layout.addRow(versao)
        layout.addRow(btn_salvar)
        # Aqui diz esta janela usará este layout
        self.setLayout(layout)

    def salvar_imovel(self):
        texto_atual = self.windowTitle()

        if texto_atual == "Sistema de Cadastro de Imóveis da Imobiliária":
            self.setWindowTitle("Clique Detectado")
        else:
            self.setWindowTitle("Sistema de Cadastro de Imóveis da Imobiliária")