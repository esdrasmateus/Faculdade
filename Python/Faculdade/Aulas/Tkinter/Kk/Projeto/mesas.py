from tkinter import *   
from PIL import Image, ImageTk
import random
from cardapio import *
import pathlib

def open_mesas():
    
    janela1 = Tk()
    janela1.title("Mesas")

    def bt1_click():
        def close_window():
            janela2.destroy()

        def open_cardapio():
            janela1.destroy()
            janela2.destroy()
            open_card()

        janela2 = Tk()
        janela2.title("Ocupada?")

        variavel = random.getrandbits(1)

        if variavel == 1:
            lb13 = Label(janela2, text = "Sim")
            lb13.grid(row = 0, column = 0)
            bt8 = Button(janela2, text = "Aperte aqui para fechar a janela", width = 30, command = close_window)
            bt8.grid(row = 1, column = 0)
            janela2.geometry("220x50+100+100")
        else:
            lb11 = Label(janela2, text = "                                                                          Não")
            lb11.grid(row = 0, column = 0)
            lb12 = Label(janela2, text = "                                                                          Você quer usar esta mesa?")
            lb12.grid(row = 1, column = 0)
            bt9 = Button(janela2, text = "Sim", width = 10, command = open_cardapio)
            bt9.grid(row = 2, column = 0)
            bt10 = Button(janela2, text = "Não", width = 10, command = close_window)
            bt10.grid(row = 2, column = 1)
            janela2.geometry("500x100+300+300")

    lb1 = Label(janela1, text = "Mesa 1: ")
    lb1.grid(row = 1, column = 0)
    cvs1 = Canvas(janela1, width = 116, height = 97)  

    bt1 = Button(janela1, width = 20, text = "Ocupada? ", command = bt1_click)
    bt1.grid(row = 2, column = 1)
    
    file_path = pathlib.Path().parent.absolute()
    path_mesa = str(file_path)
    path_imagem = path_mesa + r"\mesa.png"
    
    img1 = ImageTk.PhotoImage(Image.open(path_imagem))
    cvs1.create_image(60, 60, image=img1)
    cvs1.grid(row = 1, column = 1)

    lb2 = Label(janela1, text = "Mesa 2: ")
    lb2.grid(row = 3, column = 0)

    bt2 = Button(janela1, width = 20, text = "Ocupada? ", command = bt1_click)
    bt2.grid(row = 4, column = 1)

    cvs2 = Canvas(janela1, width = 116, height = 97)
    cvs2.create_image(60,60, image=img1)
    cvs2.grid(row = 3, column = 1)

    lb5 = Label(janela1, text = "Mesa 3: ")
    lb5.grid(row = 5, column = 0)

    bt3 = Button(janela1, width = 20, text = "Ocupada? ", command = bt1_click)
    bt3.grid(row = 6, column = 1)

    cvs3 = Canvas(janela1, width = 116, height = 97)
    cvs3.create_image(60,60, image=img1)
    cvs3.grid(row = 5, column = 1)

    lb6 = Label(janela1, text = "Mesa 4: ")
    lb6.grid(row = 7, column = 0)

    bt4 = Button(janela1, width = 20, text = "Ocupada? ", command = bt1_click)
    bt4.grid(row = 8, column = 1)

    cvs4 = Canvas(janela1, width = 116, height = 97)
    cvs4.create_image(60,60, image=img1)
    cvs4.grid(row = 7, column = 1)

    lb7 = Label(janela1, text = "Mesa 5: ")
    lb7.grid(row = 1, column = 2)

    bt5 = Button(janela1, width = 20, text = "Ocupada? ", command = bt1_click)
    bt5.grid(row = 2, column = 3)

    cvs5 = Canvas(janela1, width = 116, height = 97)
    cvs5.create_image(60,60, image=img1)
    cvs5.grid(row = 1, column = 3)

    lb8 = Label(janela1, text = "Mesa 6: ")
    lb8.grid(row = 3, column = 2)

    bt6 = Button(janela1, width = 20, text = "Ocupada? ", command = bt1_click)
    bt6.grid(row = 4, column = 3)

    cvs6 = Canvas(janela1, width = 116, height = 97)
    cvs6.create_image(60,60, image=img1)
    cvs6.grid(row = 3, column = 3)

    lb9 = Label(janela1, text = "Mesa 7: ")
    lb9.grid(row = 5, column = 2)

    bt7 = Button(janela1, width = 20, text = "Ocupada? ", command = bt1_click)
    bt7.grid(row = 6, column = 3)

    cvs7 = Canvas(janela1, width = 116, height = 97)
    cvs7.create_image(60,60, image=img1)
    cvs7.grid(row = 5, column = 3)

    lb10 = Label(janela1, text = "Mesa 8: ")
    lb10.grid(row = 7, column = 2)

    bt7 = Button(janela1, width = 20, text = "Ocupada? ", command = bt1_click)
    bt7.grid(row = 8, column = 3)

    cvs8 = Canvas(janela1, width = 116, height = 97)
    cvs8.create_image(60,60, image=img1)
    cvs8.grid(row = 7, column = 3)

    janela1.mainloop()