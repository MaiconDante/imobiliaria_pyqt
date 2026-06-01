# Arquivo principal da aplicação

# Importando Biblioteca e Classes
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication([])

window = QWidget()
# Define o título da janela
window.setWindowTitle("Sistema de Cadastro de Imóveis da Imobiliária")
# Define (LarguraxAltura) da janela
window.resize(800, 600)
# Exibi a janela
window.show()

app.exec()