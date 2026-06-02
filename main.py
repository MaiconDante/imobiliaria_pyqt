# Arquivo principal da aplicação

# Importando Biblioteca e Classes
from PyQt6.QtWidgets import QApplication
from windows import MainWindow

# Importa o estilo do arquivo externo
def load_styles(app):
    with open("styles/styles.qss", "r", encoding="utf-8") as styles:
        app.setStyleSheet(styles.read())

# Cria a aplicação
app = QApplication([])

# Carrega o estilo da janela
load_styles(app)

# Instancia janela
display_main = MainWindow()

# Exibo a tela principal
display_main.show()

# Mantém a aplicação rodando
app.exec()