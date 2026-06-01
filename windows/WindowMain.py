from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit
)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        # Define o título da janela
        self.setWindowTitle("Sistema de Cadastro de Imóveis da Imobiliária")
        # Define (LarguraxAltura) da janela
        self.resize(800, 600)
        # Cria um organizador vertical
        layout = QVBoxLayout()
        # Texto que será exibido dentro da janela - [CRIA O COMPONENTE]
        titulo = QLabel("Cadastro de Imóveis")
        layout.addWidget(titulo)
        label_codigo = QLabel("Código do Imóvel")
        input_codigo = QLineEdit()
        input_codigo.setPlaceholderText("Digite o código do Imóvel")
        layout.addWidget(label_codigo)
        layout.addWidget(input_codigo)
        label_endereco = QLabel("Endereço do Imóvel")
        input_endereco = QLineEdit()
        input_endereco.setPlaceholderText("Digite o endereço do Imóvel")
        layout.addWidget(label_endereco)
        layout.addWidget(input_endereco)
        label_cidade = QLabel("Cidade do Imóvel")
        input_cidade = QLineEdit()
        input_cidade.setPlaceholderText("Digite a cidade do Imóvel")
        layout.addWidget(label_cidade)
        layout.addWidget(input_cidade)
        informacao = QLabel("Sistema desenvolvido em PyQt6")
        versao = QLabel("Versão 1.0")
        # Adiciona o texto na janela - [COLOCA O COMPONENTE NA TELA]
        layout.addWidget(informacao)
        layout.addWidget(versao)
        # Aqui diz esta janela usará este layout
        self.setLayout(layout)