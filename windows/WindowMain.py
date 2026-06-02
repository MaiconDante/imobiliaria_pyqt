from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QWidget,
    QFormLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
    QHBoxLayout,
    QVBoxLayout,
)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.imoveis = []
        self.imovel_selecionado = None
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
        self.tabela.cellClicked.connect(self.selecionar_imovel)

        # Define o título da janela
        self.setWindowTitle("Sistema de Cadastro de Imóveis da Imobiliária")
        # Define (Largura x Altura) da janela
        self.resize(800, 600)

        # Cria container principal vertical
        main_layout = QVBoxLayout()
        header_layout = QHBoxLayout()
        form_layout = QFormLayout()
        table_layout = QFormLayout()
        buttons_layout = QHBoxLayout()
        footer_layout = QHBoxLayout()

        # [LABELS] Texto que será exibido dentro da janela - [CRIA O COMPONENTE]
        logotipo = QLabel()
        logotipo.setPixmap(QPixmap("assets/images/pyassessoria.png").scaled(40, 40))
        titulo = QLabel("Sistema de Cadastro de Imóveis")
        titulo.setObjectName("titulo")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        btn_atualizar = QPushButton("Atualizar Imóvel")
        btn_atualizar.clicked.connect(self.atualizar_imovel)
        btn_excluir = QPushButton("Excluir Imóvel")
        btn_excluir.clicked.connect(self.excluir_imovel)

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
        header_layout.addWidget(logotipo)
        header_layout.addWidget(titulo)
        form_layout.addRow(
            "Código do Imóvel:",
            self.input_codigo
        )

        form_layout.addRow(
            "Endereço do Imóvel:",
            self.input_endereco
        )

        form_layout.addRow(
            "Bairro do Imóvel:",
            self.input_bairro
        )

        form_layout.addRow(
            "Cidade do Imóvel:",
            self.input_cidade
        )
        form_layout.addRow(
            "Tipo do Imóvel:",
            self.combo_tipo
        )
        form_layout.addRow(
            "Finalidade:",
            self.combo_finalidade
        )
        form_layout.addRow(
            "Status:",
            self.combo_status
        )
        table_layout.addWidget(self.tabela)
        buttons_layout.addWidget(btn_salvar)
        buttons_layout.addWidget(btn_atualizar)
        buttons_layout.addWidget(btn_excluir)
        footer_layout.addWidget(informacao)
        footer_layout.addWidget(versao)

        # Enviando tudo ja organizado
        main_layout.addLayout(header_layout)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(table_layout)
        main_layout.addLayout(buttons_layout)
        main_layout.addLayout(footer_layout)

        # Aqui diz esta janela usará este layout
        self.setLayout(main_layout)

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
        
    def selecionar_imovel(self, linha, coluna):
         
         self.imovel_selecionado = linha 
         imovel = self.imoveis[linha]

         self.input_codigo.setText(imovel["codigo"])
         self.input_endereco.setText(imovel["endereco"])
         self.input_bairro.setText(imovel["bairro"])
         self.input_cidade.setText(imovel["cidade"])
         self.combo_tipo.setCurrentText(imovel["tipo"])
         self.combo_finalidade.setCurrentText(imovel["finalidade"])
         self.combo_status.setCurrentText(imovel["status"])

    def atualizar_imovel(self):

        if self.imovel_selecionado is None:
            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione um imóvel na tabela para atualizar."
            )
            return
        
        if not self.validar_campos():
            return
        
        dados = self.obter_dados_formulario()
        self.imoveis[self.imovel_selecionado] = dados
        self.atualizar_tabela()

        QMessageBox.information(
            self,
            "Sucesso",
            "Imóvel atualizado com sucesso!"
        )

        self.limpar_campos()
        self.imovel_selecionado = None

    def excluir_imovel(self):

        if self.imovel_selecionado is None:
            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione um imóvel para excluir."
            )
            return
        
        resposta = QMessageBox.question(
                self,
                "Confirmação",
                "Tem certeza que deseja excluir este imóvel?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if resposta != QMessageBox.StandardButton.Yes:
            return
        
        del self.imoveis[self.imovel_selecionado]
        self.atualizar_tabela()
        self.limpar_campos()
        self.imovel_selecionado = None

        QMessageBox.information(
            self,
            "Sucesso",
            "Imóvel excluído com sucesso!"
        )
    