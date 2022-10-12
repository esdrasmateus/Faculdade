from tkinter import *
from mesas import *
from PIL import Image,ImageTk
import pathlib

lista1 = []
lista2 = []

vazio = str("")

file_path = pathlib.Path().parent.absolute()

path_logo = str(file_path)
path_imagem1 = path_logo + r"\Imagens\logo.png"

def bt2_press():
    def lista():
        if str(regusuario.get()) == vazio or str(regsenha.get()) == vazio:
            label2 ["text"] = "O usuario ou a senha nao podem ser vazios"
        else:
            lista1.append(regusuario.get())
            lista2.append(regsenha.get())
            janela2.destroy()

    janela2 = Tk()
    janela2.title("Registrar-se")
    regusuario = Entry(janela2)
    regusuario.grid(row = 0, column = 1)

    regusuario_label = Label(janela2, text = "              Usuario")
    regusuario_label.grid (row = 0, column = 0)

    regsenha = Entry(janela2)
    regsenha.grid(row = 1, column = 1)

    regsenha_label = Label(janela2, text = "               Senha")
    regsenha_label.grid(row = 1, column = 0)

    regbt = Button(janela2, width = 20, text = "Registrar-se", command = lista)
    regbt.grid(row = 3, column = 1)
    
    label2 = Label(janela2, text = "Pressione em 'Registrar-se' apos digitar seus dados")
    label2.grid(row = 4, column = 0)
    
    janela2.geometry("500x100+300+300")

def login():
    if (usuario.get() in lista1 and senha.get() in lista2):
        janela1.destroy()
        open_mesas()
    elif str(usuario.get()) == vazio or str(senha.get()) == vazio:
        label1["text"] = "O login ou a senha nao pode ser vazio!"
    else:
        label1["text"] = "Login mal-sucedido"

def show_pass():
    if (check_var.get()):
        senha.configure(show = "")
    else:
        senha.configure(show = "*")

janela1 = Tk()
janela1.title("Login")

bem_vindo_label = Label(janela1, text = "Seja Bem Vindo ao restaurante da Tia Lia")
bem_vindo_label.grid(row = 0, column = 0)

usuario = Entry(janela1)
usuario.grid(row = 1, column = 1)

usuario_label = Label(janela1, text = "Usuario: ")
usuario_label.grid(row = 1, column = 0)

senha = Entry(janela1, show = "*")
senha.grid(row = 2, column = 1)
senha_label = Label(janela1, text = "Senha: ")
senha_label.grid(row = 2, column = 0)

check_var = IntVar()
check_box1 = Checkbutton(janela1, command = show_pass, variable = check_var, text = "Mostrar senha")
check_box1.grid(row = 2, column = 2)

bt1 = Button(janela1, width = 20, text = "Confirmar", command = login)
bt1.grid(row = 3, column = 1)

bt2 = Button(janela1, width = 20, text = "Registrar um novo usuario", command = bt2_press)
bt2.grid(row = 4, column = 1)

cnvs1 = Canvas(janela1, width = 310, height = 163)
img1 = ImageTk.PhotoImage(Image.open(path_imagem1))
cnvs1.create_image(60, 60, image = img1)
cnvs1.grid(row = 2, column = 3)

label1 = Label(janela1, text = "Aguardando dados")
label1.grid(row = 5, column = 1)

janela1.geometry("600x300+300+300")

janela1.mainloop()