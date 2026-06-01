from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
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
        informacao = QLabel("Sistema desenvolvido em PyQt6")
        versao = QLabel("Versão 1.0")
        # Adiciona o texto na janela - [COLOCA O COMPONENTE NA TELA]
        layout.addWidget(titulo)
        layout.addWidget(informacao)
        layout.addWidget(versao)
        # Aqui diz esta janela usará este layout
        self.setLayout(layout)