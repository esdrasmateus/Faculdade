from tkinter import *
from PIL import Image, ImageTk
import pathlib

def open_card():
    janela1 = Tk()
    janela1.title("Cardapio")
    total = []
    
    lb9 = Label(janela1, text = total)
    lb9.grid(row = 1, column = 3)
    
    def stro12():
        total.append(float(12.50))
        lb9['text'] = total
        lb9.grid(row = 5, column = 3)
        def soma_lista():

            def destroyxD():
                exit()

            janela2 = Toplevel()
            janela2.title("Pagamento")
            lb10 = Label(janela2, text = "O seu total e R$ " + str(sum(total)))
            lb10.grid(row = 0, column = 1)
            janela2.geometry("300x100+300+300")
            bt11 = Button(janela2, width = 20, command = destroyxD, text = "Pagar a conta")
            bt11.grid(row = 1, column = 1)
        bt9 = Button(janela1, text = "Calcular Total", width = 20, command = soma_lista)
        bt9.grid(row = 5, column = 0)
        bt10 = Button(janela1, width = 20, text = "Limpar pedido", command = reset_lista)
        bt10.grid(row = 5, column = 1)
        
    def las20():
        total.append(float(21.00))
        lb9['text'] = total
        lb9.grid(row = 5, column = 3)
        def soma_lista():

            def destroyxD():
                exit()

            janela2 = Toplevel()
            janela2.title("Pagamento")
            lb10 = Label(janela2, text = "O seu total e R$ " + str(sum(total)))
            lb10.grid(row = 0, column = 1)
            janela2.geometry("300x100+300+300")
            bt11 = Button(janela2, width = 20, command = destroyxD, text = "Pagar a conta")
            bt11.grid(row = 1, column = 1)
        bt9 = Button(janela1, text = "Calcular Total", width = 20, command = soma_lista)
        bt9.grid(row = 5, column = 0)
        bt10 = Button(janela1, width = 20, text = "Limpar pedido", command = reset_lista)
        bt10.grid(row = 5, column = 1)

    def parm34():
        total.append(float(34.50))
        lb9['text'] = total
        lb9.grid(row = 5, column = 3)
        def soma_lista():

            def destroyxD():
                exit()

            janela2 = Toplevel()
            janela2.title("Pagamento")
            lb10 = Label(janela2, text = "O seu total e R$ " + str(sum(total)))
            lb10.grid(row = 0, column = 1)
            janela2.geometry("300x100+300+300")
            bt11 = Button(janela2, width = 20, command = destroyxD, text = "Pagar a conta")
            bt11.grid(row = 1, column = 1)
        bt9 = Button(janela1, text = "Calcular Total", width = 20, command = soma_lista)
        bt9.grid(row = 5, column = 0)
        bt10 = Button(janela1, width = 20, text = "Limpar pedido", command = reset_lista)
        bt10.grid(row = 5, column = 1)

    def sald15():
        total.append(float(15.00))
        lb9['text'] = total
        lb9.grid(row = 5, column = 3)
        def soma_lista():

            def destroyxD():
                exit()

            janela2 = Toplevel()
            janela2.title("Pagamento")
            lb10 = Label(janela2, text = "O seu total e R$ " + str(sum(total)))
            lb10.grid(row = 0, column = 1)
            janela2.geometry("300x100+300+300")
            bt11 = Button(janela2, width = 20, command = destroyxD, text = "Pagar a conta")
            bt11.grid(row = 1, column = 1)
        bt9 = Button(janela1, text = "Calcular Total", width = 20, command = soma_lista)
        bt9.grid(row = 5, column = 0)
        bt10 = Button(janela1, width = 20, text = "Limpar pedido", command = reset_lista)
        bt10.grid(row = 5, column = 1)

    def coca10():
        total.append(float(10.00))
        lb9['text'] = total
        lb9.grid(row = 5, column = 3)
        def soma_lista():

            def destroyxD():
                exit()

            janela2 = Toplevel()
            janela2.title("Pagamento")
            lb10 = Label(janela2, text = "O seu total e R$ " + str(sum(total)))
            lb10.grid(row = 0, column = 1)
            janela2.geometry("300x100+300+300")
            bt11 = Button(janela2, width = 20, command = destroyxD, text = "Pagar a conta")
            bt11.grid(row = 1, column = 1)
        bt9 = Button(janela1, text = "Calcular Total", width = 20, command = soma_lista)
        bt9.grid(row = 5, column = 0)
        bt10 = Button(janela1, width = 20, text = "Limpar pedido", command = reset_lista)
        bt10.grid(row = 5, column = 1)

    def hein12():
        total.append(float(12.00))
        lb9['text'] = total
        lb9.grid(row = 5, column = 3)
        def soma_lista():

            def destroyxD():
                exit()

            janela2 = Toplevel()
            janela2.title("Pagamento")
            lb10 = Label(janela2, text = "O seu total e R$ " + str(sum(total)))
            lb10.grid(row = 0, column = 1)
            janela2.geometry("300x100+300+300")
            bt11 = Button(janela2, width = 20, command = destroyxD, text = "Pagar a conta")
            bt11.grid(row = 1, column = 1)
        bt9 = Button(janela1, text = "Calcular Total", width = 20, command = soma_lista)
        bt9.grid(row = 5, column = 0)
        bt10 = Button(janela1, width = 20, text = "Limpar pedido", command = reset_lista)
        bt10.grid(row = 5, column = 1)

    def suco10():
        total.append(float(10.00))
        lb9['text'] = total
        lb9.grid(row = 5, column = 3)
        def soma_lista():

            def destroyxD():
                exit()

            janela2 = Toplevel()
            janela2.title("Pagamento")
            lb10 = Label(janela2, text = "O seu total e R$ " + str(sum(total)))
            lb10.grid(row = 0, column = 1)
            janela2.geometry("300x100+300+300")
            bt11 = Button(janela2, width = 20, command = destroyxD, text = "Pagar a conta")
            bt11.grid(row = 1, column = 1)
        bt9 = Button(janela1, text = "Calcular Total", width = 20, command = soma_lista)
        bt9.grid(row = 5, column = 0)
        bt10 = Button(janela1, width = 20, text = "Limpar pedido", command = reset_lista)
        bt10.grid(row = 5, column = 1)

    def agua75():
        total.append(float(7.50))
        lb9['text'] = total
        lb9.grid(row = 5, column = 3)
        def soma_lista():

            def destroyxD():
                exit()

            janela2 = Toplevel()
            janela2.title("Pagamento")
            lb10 = Label(janela2, text = "O seu total e R$ " + str(sum(total)))
            lb10.grid(row = 0, column = 1)
            janela2.geometry("300x100+500+500")
            bt11 = Button(janela2, width = 20, command = destroyxD, text = "Pagar a conta")
            bt11.grid(row = 1, column = 1)
        bt9 = Button(janela1, text = "Calcular Total", width = 20, command = soma_lista)
        bt9.grid(row = 5, column = 0)
        bt10 = Button(janela1, width = 20, text = "Limpar pedido", command = reset_lista)
        bt10.grid(row = 5, column = 1) 

    def reset_lista():
        total.clear()
        lb9['text'] = total
    
    file_path = pathlib.Path().parent.absolute()
    
    path_strogonoff = str(file_path)
    path_imagem1 = path_strogonoff + r"\Imagens\strogonoff.png"
    
    path_lasanha = str(file_path)
    path_imagem2 = path_lasanha + r"\Imagens\lasanha.png"
    
    path_parmegiana = str(file_path)
    path_imagem3 = path_parmegiana + r"\Imagens\parmegiana.png"
    
    path_salada = str(file_path)
    path_imagem4= path_salada + r"\Imagens\salada.png"
    
    path_coca = str(file_path)
    path_imagem5 = path_coca + r"\Imagens\coca.png"
    
    path_heineken = str(file_path)
    path_imagem6 = path_heineken + r"\Imagens\heineken.png"
    
    path_suco = str(file_path)
    path_imagem7 = path_suco + r"\Imagens\suco.png"
    
    path_agua = str(file_path)
    path_imagem8 = path_agua + r"\Imagens\agua.png"
    
    cnvs1 = Canvas(janela1, width = 116, height = 116)
    img1 = ImageTk.PhotoImage(Image.open(path_imagem1))
    cnvs1.create_image(60, 60, image = img1)
    cnvs1.grid(row = 0, column = 1)

    cnvs2 = Canvas(janela1, width = 116, height = 116)
    img2 = ImageTk.PhotoImage(Image.open(path_imagem2))
    cnvs2.create_image(60, 60, image = img2)
    cnvs2.grid(row = 1, column = 1)

    cnvs3 = Canvas(janela1, width = 116, height = 116)
    img3 = ImageTk.PhotoImage(Image.open(path_imagem3))
    cnvs3.create_image(60, 60, image = img3)
    cnvs3.grid(row = 2, column = 1)

    cnvs4 = Canvas(janela1, width = 116, height = 116)
    img4 = ImageTk.PhotoImage(Image.open(path_imagem4))
    cnvs4.create_image(60, 60, image = img4)
    cnvs4.grid(row = 3, column = 1)

    cnvs5 = Canvas(janela1, width = 116, height = 116)
    img5 = ImageTk.PhotoImage(Image.open(path_imagem5))
    cnvs5.create_image(60, 60, image = img5)
    cnvs5.grid(row = 0, column = 4)

    cnvs6 = Canvas(janela1, width = 116, height = 116)
    img6 = ImageTk.PhotoImage(Image.open(path_imagem6))
    cnvs6.create_image(60, 60, image = img6)
    cnvs6.grid(row = 1, column = 4)

    cnvs7 = Canvas(janela1, width = 116, height = 116)
    img7 = ImageTk.PhotoImage(Image.open(path_imagem7))
    cnvs7.create_image(60, 60, image = img7)
    cnvs7.grid(row = 2, column = 4)

    cnvs8 = Canvas(janela1, width = 116, height = 116)
    img8 = ImageTk.PhotoImage(Image.open(path_imagem8))
    cnvs8.create_image(60, 60, image = img8)
    cnvs8.grid(row = 3, column = 4)

    lb1 = Label(janela1, text = "Strogonoff de Frango")
    lb1.grid(row = 0, column = 0)

    bt1 = Button(janela1, text = "R$ 12.50", width = 20, command = stro12)
    bt1.grid(row = 0, column = 2)

    lb2 = Label(janela1, text = "Lasanha a Bolonhesa")
    lb2.grid(row = 1, column = 0)

    bt2 = Button(janela1, text = "R$ 21.00", width = 20, command = las20)
    bt2.grid(row = 1, column = 2)

    lb3 = Label(janela1, text = "Parmegiana de Frango (4 Pessoas)")
    lb3.grid(row = 2, column = 0)

    bt3 = Button(janela1, text = "R$ 34.50", width = 20, command = parm34)
    bt3.grid(row = 2, column = 2)

    lb4 = Label(janela1, text = "Salada Caesar Vegana")
    lb4.grid(row = 3, column = 0)

    bt4 = Button(janela1, text = "R$ 15.00", width = 20, command = sald15)
    bt4.grid(row = 3, column = 2)

    lb5 = Label(janela1, text = "Coca-Cola (2L)")
    lb5.grid(row = 0, column = 3)

    bt5 = Button(janela1, text = "R$ 10.00", width = 20, command = coca10)
    bt5.grid(row = 0, column = 5)

    lb6 = Label(janela1, text = "Heineken")
    lb6.grid(row = 1, column = 3)

    bt6 = Button(janela1, text = "R$ 12.00", width = 20, command = hein12)
    bt6.grid(row = 1, column = 5)

    lb7 = Label(janela1, text = "   Suco de Laranja (1L)")
    lb7.grid(row = 2, column = 3)

    bt7 = Button(janela1, text = "R$ 10.00", width = 20, command = suco10)
    bt7.grid(row = 2, column = 5)

    lb8 = Label(janela1, text = "Agua")
    lb8.grid(row = 3, column = 3)

    bt8 = Button(janela1, text = "R$ 7.50", width = 20, command = agua75)
    bt8.grid(row = 3, column = 5)
    
    janela1.geometry("+300+300")
    janela1.mainloop()