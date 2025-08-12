from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
#----------------------------------------------------------------------------------------------
def login():
    janela_login = QWidget()
    janela_login.resize(310, 350) # Criar janela Login
    janela_login.setStyleSheet("background-color: lightblue;")
    janela_login.setWindowTitle("Login")
    #----------------------------------------------------------------------------------------------
    layout = QVBoxLayout()

    titulo = QLabel("LOGIN")
    titulo.setAlignment(Qt.AlignmentFlag.AlignCenter) # Centralizar o login no meio
    titulo.setStyleSheet("font-size: 24px; font-weight: bold;")
    layout.addWidget(titulo)
    #----------------------------------------------------------------------------------------------
    linha = QFrame()
    linha.setFrameShape(QFrame.Shape.HLine) # Criação de linha azul
    linha.setStyleSheet("color: blue; background-color: blue; height: 2px;")
    layout.addWidget(linha)
    #----------------------------------------------------------------------------------------------
    layout.addSpacing(25)

    email = QLineEdit()
    email.setPlaceholderText("Email") # Caixa de texto email
    email.setStyleSheet("background-color: white;")
    layout.addWidget(email)
    #----------------------------------------------------------------------------------------------
    layout.addSpacing(20)

    senha = QLineEdit()
    senha.setPlaceholderText("Senha") # Caixa de texto senha
    senha.setEchoMode(QLineEdit.EchoMode.Password) # Ocultar a senha
    senha.setStyleSheet("background-color: white;")
    layout.addWidget(senha)
    #----------------------------------------------------------------------------------------------
    layout.addSpacing(120)


    def verificar_login(): # mudar nome de verificar para verificar_login
        if email.text() == "" or senha.text() == "":
            QMessageBox.warning(janela_login, "Erro", "O campo não pode estar vazio!")
        else:            # verificar se há campos vazios
            janela_login.close() # fecha a pagina
            entrada()

    botao_login = QPushButton("Entrar")
    botao_login.setStyleSheet("background-color: skyblue;")
    botao_login.clicked.connect(verificar_login) # Botao entra que se liga a entrada
    layout.addWidget(botao_login)

    botao_cadastro = QPushButton("Não tenho cadastro")
    botao_cadastro.setStyleSheet("background-color: skyblue;")
    botao_cadastro.clicked.connect(cadastro)
    layout.addWidget(botao_cadastro)

    janelas_abertas.append(janela_login)
    #----------------------------------------------------------------------------------------------

    janela_login.setLayout(layout)
    janela_login.show()


def cadastro():
    janela_cadastro = QWidget()
    janela_cadastro.setWindowTitle("Cadastro") # Criar janela de cadastro
    janela_cadastro.resize(310, 350)
    janela_cadastro.setStyleSheet("background-color: lightblue;")
#----------------------------------------------------------------------------------------------
    layout_cadastro = QVBoxLayout()

    titulo = QLabel("CADASTRO")
    titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
    titulo.setStyleSheet("font-size: 24px; font-weight: bold;")
    layout_cadastro.addWidget(titulo)
#----------------------------------------------------------------------------------------------

    linha = QFrame()
    linha.setFrameShape(QFrame.Shape.HLine) # linhas azul
    linha.setStyleSheet("color: blue; background-color: blue; height: 2px;")
    layout_cadastro.addWidget(linha)
#----------------------------------------------------------------------------------------------
    layout_cadastro.addSpacing(20)

    nome_completo = QLineEdit() # Caixa de texto nome 
    nome_completo.setPlaceholderText("Nome completo")
    nome_completo.setStyleSheet("background-color: white;")
    layout_cadastro.addWidget(nome_completo)
#----------------------------------------------------------------------------------------------
    layout_cadastro.addSpacing(25)

    email = QLineEdit()
    email.setPlaceholderText("Email") # Caixa de texto email
    email.setStyleSheet("background-color: white;")
    layout_cadastro.addWidget(email)
#----------------------------------------------------------------------------------------------
    layout_cadastro.addSpacing(25)

    senha = QLineEdit()
    senha.setPlaceholderText("Senha") # caixa de texto senha
    senha.setEchoMode(QLineEdit.EchoMode.Password) # ocultar a senha
    senha.setStyleSheet("background-color: white;")
    layout_cadastro.addWidget(senha)
#----------------------------------------------------------------------------------------------
    
    def verificar_cadastro():
        if nome_completo.text() == "" or email.text() == "" or senha.text() == "":
            QMessageBox.warning(janela_cadastro, "Erro", "O campo não pode estar vazio!")
        else:# verificar se há campos vazios
            janela_cadastro.close()  # fecha a pagina
            login()
    
    layout_cadastro.addSpacing(25)


    botao_cadastrar = QPushButton("Cadastrar")
    botao_cadastrar.setStyleSheet("background-color: skyblue;")
    layout_cadastro.addWidget(botao_cadastrar)
    botao_cadastrar.clicked.connect(verificar_cadastro)
#----------------------------------------------------------------------------------------------

    janela_cadastro.setLayout(layout_cadastro)
    janela_cadastro.show()

    janelas_abertas.append(janela_cadastro)
#----------------------------------------------------------------------------------------------

def entrada():
    janela_inicio = QWidget()
    janela_inicio.setWindowTitle("Você entrou!!!")
    janela_inicio.resize(310, 350) # Criar janela de início
    janela_inicio.setStyleSheet("background-color: lightblue;")

    layout_entrada = QVBoxLayout() # layout definido de cima para baixo
#----------------------------------------------------------------------------------------------
    texto = QLabel("Você entrou com sucesso!")
    texto.setAlignment(Qt.AlignmentFlag.AlignCenter)
    texto.setStyleSheet("font-size: 18px; font-weight: bold;")
    layout_entrada.addWidget(texto)
              # Texto de entrada no início
    janela_inicio.setLayout(layout_entrada)
    janela_inicio.show()

    janelas_abertas.append(janela_inicio)
#----------------------------------------------------------------------------------------------


app = QApplication([])

janelas_abertas = []

login()

app.exec()