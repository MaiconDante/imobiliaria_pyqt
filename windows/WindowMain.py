from PyQt6.QtWidgets import (
    QWidget,
    QFormLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem
)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.imoveis = []
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(7)
        self.tabela.setHorizontalHeaderLabels([
            "Código",
            "Endereço",
            "Cidade",
            "Bairro",
            "Tipo",
            "Finalidade",
            "Status"
        ])

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
        # [COMBOBOX] Adiciona campo de escolhas de opções
        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems([
            "Selecione uma opção",
            "Casa",
            "Apartamento",
            "Terreno"
        ])
        self.combo_tipo.setCurrentText("Selecione uma opção")
        self.combo_finalidade = QComboBox()
        self.combo_finalidade.addItems([
            "Selecione uma opção",
            "Venda",
            "Locação",
            "Venda e Locação"
        ])
        self.combo_finalidade.setCurrentText("Selecione uma opção") # Apenas para saber se quiser priorizar alguma opção
        self.combo_status = QComboBox()
        self.combo_status.addItems([
            "Selecione uma opção",
            "Disponível",
            "Locado",
            "Vendido",
            "A Liberar"
        ])
        self.combo_status.setCurrentText("Selecione uma opção")
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
        layout.addRow(
            "Tipo do Imóvel:",
            self.combo_tipo
        )
        layout.addRow(
            "Finalidade:",
            self.combo_finalidade
        )
        layout.addRow(
            "Status:",
            self.combo_status
        )
        layout.addRow(informacao)
        layout.addRow(versao)
        layout.addRow(self.tabela)
        layout.addRow(btn_salvar)

        # Aqui diz esta janela usará este layout
        self.setLayout(layout)

    def validar_campos(self):

        if not self.input_codigo.text():
            QMessageBox.warning(
                self,
                "Atenção",
                "Informe o código do imóvel."
            )
            return False

        if not self.input_endereco.text():
            QMessageBox.warning(
                self,
                "Atenção",
                "Informe o endereço do imóvel."
            )
            return False

        if not self.input_bairro.text():
            QMessageBox.warning(
                self,
                "Atenção",
                "Informe o bairro do imóvel."
            )
            return False

        if not self.input_cidade.text():
            QMessageBox.warning(
                self,
                "Atenção",
                "Informe a cidade do imóvel."
            )
            return False

        if self.combo_tipo.currentText() == "Selecione uma opção":
            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione o tipo do imóvel."
            )
            return False

        if self.combo_finalidade.currentText() == "Selecione uma opção":
            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione a finalidade."
            )
            return False

        if self.combo_status.currentText() == "Selecione uma opção":
            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione o status do imóvel."
            )
            return False

        return True
                

    def obter_dados_formulario(self):

        dados = {
            "codigo": self.input_codigo.text(),
            "endereco": self.input_endereco.text(),
            "cidade": self.input_cidade.text(),
            "bairro": self.input_bairro.text(),
            "tipo": self.combo_tipo.currentText(),
            "finalidade": self.combo_finalidade.currentText(),
            "status": self.combo_status.currentText()
        }

        return dados
    
    def limpar_campos(self):
        self.input_codigo.clear()
        self.input_endereco.clear()
        self.input_bairro.clear()
        self.input_cidade.clear()
        self.combo_tipo.setCurrentIndex(0)
        self.combo_finalidade.setCurrentIndex(0)
        self.combo_status.setCurrentIndex(0)

    def salvar_imovel(self):

        if not self.validar_campos():
            return

        dados = self.obter_dados_formulario()
        self.imoveis.append(dados)
        self.atualizar_tabela()

        QMessageBox.information(
            self,
            "Sucesso",
            "Imóvel validado com sucesso."
        )
        self.limpar_campos()

    def atualizar_tabela(self):

        self.tabela.setRowCount(len(self.imoveis))

        for linha, imovel in enumerate(self.imoveis):

            self.tabela.setItem(linha, 0, QTableWidgetItem(imovel["codigo"]))
            self.tabela.setItem(linha, 1, QTableWidgetItem(imovel["endereco"]))
            self.tabela.setItem(linha, 2, QTableWidgetItem(imovel["cidade"]))
            self.tabela.setItem(linha, 3, QTableWidgetItem(imovel["bairro"]))
            self.tabela.setItem(linha, 4, QTableWidgetItem(imovel["tipo"]))
            self.tabela.setItem(linha, 5, QTableWidgetItem(imovel["finalidade"]))
            self.tabela.setItem(linha, 6, QTableWidgetItem(imovel["status"]))
        