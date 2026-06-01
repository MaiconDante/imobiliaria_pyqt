# Arquivo principal da aplicação

# Importando Biblioteca e Classes
from PyQt6.QtWidgets import QApplication
from windows import MainWindow

# Cria a aplicação
app = QApplication([])

# Instancia janela
display_main = MainWindow()

# Exibo a tela principal
display_main.show()

# Mantém a aplicação rodando
app.exec()