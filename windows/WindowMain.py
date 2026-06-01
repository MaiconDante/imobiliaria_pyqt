from PyQt6.QtWidgets import QWidget

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        # Define o título da janela
        self.setWindowTitle("Sistema de Cadastro de Imóveis da Imobiliária")
        # Define (LarguraxAltura) da janela
        self.resize(800, 600)