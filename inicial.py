from tkinter import *

def semComando():
    print("")

def tela_nova_sala():
    tela_nova_sala = Toplevel(app)
    tela_nova_sala.title("Cadastro de salas".title())
    tela_nova_sala.geometry("400x100")
    tela_nova_sala.configure(bg="#dde")

    Label(tela_nova_sala, text="Nome:", bg="#dde", anchor=W).place(x=10, y=10, width=45, height=20)
    vnome_sala = Entry(tela_nova_sala)
    vnome_sala.place(x=60, y=10, width=100, height=20)

    Label(tela_nova_sala, text="Tipo:", bg="#dde", anchor=W).place(x=170, y=10, width=70, height=20)
    vtipo_sala = Entry(tela_nova_sala)
    vtipo_sala.place(x=210, y=10, width=50, height=20)

    Label(tela_nova_sala, text="Lotação:", bg="#dde", anchor=W).place(x=10, y=40, width=50, height=20)
    vlotacao_sala = Entry(tela_nova_sala)
    vlotacao_sala.place(x=70, y=40, width=30, height=20)

    Button(tela_nova_sala, text="Cadastrar", command=botao_nova_sala).place(x=335, y=70, width=60, height=25)

def botao_nova_sala():
    print()

def tela_novo_aluno():
    tela_novo_aluno = Toplevel(app)
    tela_novo_aluno.title("Cadastro De Alunos".title())
    tela_novo_aluno.geometry("470x265")
    tela_novo_aluno.configure(bg="#dde")

    Label(tela_novo_aluno, text="Nome:", bg="#dde", anchor=W).place(x=10, y=10, width=45, height=20)
    vnome = Entry(tela_novo_aluno)
    vnome.place(x=60, y=10, width=100, height=20)

    Label(tela_novo_aluno, text="Sobrenome:", bg="#dde", anchor=W).place(x=170, y=10, width=70, height=20)
    vsobrenome = Entry(tela_novo_aluno)
    vsobrenome.place(x=245, y=10, width=200, height=20)

    Label(tela_novo_aluno, text="Contato:", bg="#dde", anchor=W).place(x=10, y=40, width=50, height=20)
    vfone = Entry(tela_novo_aluno)
    vfone.place(x=70, y=40, width=110, height=20)

    Label(tela_novo_aluno, text="E-mail:", bg="#dde", anchor=W).place(x=190, y=40, width=50, height=20)
    vemail = Entry(tela_novo_aluno)
    vemail.place(x=245, y=40, width=200, height=20)

    Label(tela_novo_aluno, text="Sala:", bg="#dde", anchor=W).place(x=10, y=70, width=50, height=20)
    vsala = Entry(tela_novo_aluno)
    vsala.place(x=50, y=70, width=110, height=20)

    Label(tela_novo_aluno, text="Observações:", bg="#dde", anchor=W).place(x=10, y=100, width=80, height=20)
    vobs = Text(tela_novo_aluno)
    vobs.place(x=10, y=120, width=450, height=100)

    Button(tela_novo_aluno, text="Cadastrar", command=botao_novo_aluno).place(x=400, y=230, width=60, height=25)

def botao_novo_aluno():
    print("")

app = Tk()
app.title("Gestor")
app.geometry("500x300")
app.configure(bg="#dde")

#menu de cadastros
barraDeMenus = Menu(app)
menuCadastros = Menu(barraDeMenus, tearoff=0)
menuCadastros.add_command(label="Salas", command=tela_nova_sala)
menuCadastros.add_command(label="Alunos", command=tela_novo_aluno)
menuCadastros.add_separator()
menuCadastros.add_command(label="Fechar", command=app.quit)
barraDeMenus.add_cascade(label="Cadastros", menu=menuCadastros)

#menu de consultas
menuConsultas = Menu(barraDeMenus, tearoff=0)
menuConsultas.add_command(label="Alunos", command=semComando)
menuConsultas.add_command(label="Salas", command=semComando)
barraDeMenus.add_cascade(label="Pesquisar", menu=menuConsultas)

#menuSobre
menuSobre = Menu(barraDeMenus, tearoff=0)
menuSobre.add_command(label="Ajuda",command=semComando)
menuSobre.add_command(label="Sobre",command=semComando)
barraDeMenus.add_cascade(label="Sobre",menu=menuSobre)

app.config(menu=barraDeMenus)

app.mainloop()