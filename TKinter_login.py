from tkinter import *
from tkinter import messagebox

def entrada():
    janela_inicio = Tk()
    janela_inicio.geometry('310x350')
    janela_inicio.title("Início") # Criação da janela login
    janela_inicio.configure(bg="lightblue")
    mensagem = Label(janela_inicio, text="Bem-vindo à tela inicial!", font=("Arial", 16), bg="Skyblue")
    mensagem.pack(pady=(50, 0))
    janela_inicio.mainloop()
#----------------------------------------------------------------------------------------------
def cadastro():
    janela_cadastrar = Tk()
    janela_cadastrar.geometry('310x350')
    janela_cadastrar.title("Cadastro") #Criação da janela cadastro
    janela_cadastrar.configure(bg="lightblue")
    titulo = Label(janela_cadastrar, text="CADASTRO", bg="lightblue", font=("Arial", 24, "bold"))
    titulo.pack(pady=20)
#----------------------------------------------------------------------------------------------
    linha_azul = Frame(janela_cadastrar, height=2, bg="blue")
    linha_azul.pack(fill="x", padx=20, pady=10) # linha azul
#----------------------------------------------------------------------------------------------
    frame_nome = Frame(janela_cadastrar)
    frame_nome.pack(fill="x", padx=20) # frame que contem nome e sobrenome
    nome = Label(frame_nome, text="Nome e sobrenome", font=("Arial", 12, "bold"))
    nome.pack(anchor="w")

    texto_nome = Entry(janela_cadastrar, width=50) # caixa de texto nome e sobrenome
    texto_nome.pack(padx=20)
#----------------------------------------------------------------------------------------------
    frame_email = Frame(janela_cadastrar)
    frame_email.pack(fill="x", padx=20, pady=(20, 0)) #frame que contem email
    email = Label(frame_email, text="Email", font=("Arial", 12, "bold"))
    email.pack(anchor="w")

    texto_email = Entry(janela_cadastrar, width=50)# caixa de texto email
    texto_email.pack(padx=20)
#----------------------------------------------------------------------------------------------
    frame_senha = Frame(janela_cadastrar)
    frame_senha.pack(fill="x", padx=20, pady=(20, 0))# frame que contem senha
    senha = Label(frame_senha, text="Senha", font=("Arial", 12, "bold"))
    senha.pack(anchor="w")

    texto_senha = Entry(janela_cadastrar, width=50, show="*") # caixa de texto senha que oculta os caracteres
    texto_senha.pack(padx=20, anchor="w")
#----------------------------------------------------------------------------------------------
    def verificar_cadastro():
        nome = texto_nome.get()
        email = texto_email.get()
        senha = texto_senha.get()      # verificar se há algum campo vazio
        if nome == "" or email == "" or senha == "":
            messagebox.showerror("Erro", "Preencha todos os campos!")
        else:
            janela_cadastrar.destroy()
            login()
#----------------------------------------------------------------------------------------------
    login_botao = Button(janela_cadastrar, text= "Login", bg = "skyblue", command=verificar_cadastro)
    login_botao.pack(padx= 20, pady=(20, 0))# botao login
     
    janela_cadastrar.mainloop()
#----------------------------------------------------------------------------------------------
def login():
    janela_login = Tk() #mudar nome de janela para janela_login
    janela_login.title("login")
    janela_login.geometry('310x350')
    janela_login.configure(bg="lightblue")
#----------------------------------------------------------------------------------------------
    titulo = Label(janela_login, text="LOGIN", bg="lightblue", font=("Arial", 24, "bold"))
    titulo.pack(pady=20) # titulo login
#----------------------------------------------------------------------------------------------
    linha = Frame(janela_login, height=2, bd=0, bg="blue") # linha azul
    linha.pack(fill="x", padx=20, pady=10)
#----------------------------------------------------------------------------------------------
    frame_email = Frame(janela_login)
    frame_email.pack(fill="x", padx=20) # frame que contem email
    email = Label(frame_email, text="Email", font=("Arial", 12, "bold"))
    email.pack(anchor="w")

    texto_email = Entry(janela_login, width=50)
    texto_email.pack(padx=20, anchor="w")# caixa de texto email
#----------------------------------------------------------------------------------------------
    frame_senha = Frame(janela_login)
    frame_senha.pack(fill="x", padx=20, pady=(45, 0))# frame que contem senha
    senha = Label(frame_senha, text="Senha", font=("Arial", 12, "bold"))
    senha.pack(anchor="w")

    texto_senha = Entry(janela_login, width=50, show="*")# caixa de texto senha que oculta os caracteres
    texto_senha.pack(padx=20, anchor="w")
#----------------------------------------------------------------------------------------------
    def verificar_login():
        email = texto_email.get()
        senha = texto_senha.get()
        if email == "" or senha == "":   # verificar se há algum campo vazio
            messagebox.showerror("Erro", "Preencha todos os campos!")
        else:
            janela_login.destroy()
            entrada()
#----------------------------------------------------------------------------------------------
    entrar = Button(janela_login, text="Entrar", bg="skyblue", command=verificar_login)
    entrar.pack(padx=20, pady=(30, 0))
#----------------------------------------------------------------------------------------------
    sem_cadastro = Button(janela_login, text="Não tenho cadastro", bg="blue", font=("Arial", 12), fg="skyblue", command=cadastro)
    sem_cadastro.pack(padx=20, pady=(12, 0))
#----------------------------------------------------------------------------------------------
    janela_login.mainloop()

login()