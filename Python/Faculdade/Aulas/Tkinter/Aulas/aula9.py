from tkinter import *

janela = Tk()

def bt_click():
    print("Clickou")
    if (str(et1.get()).isnumeric() and str(et2.get()) .isnumeric()):
        num1 = int(et1.get())
        num2 = int(et2.get())

        lb["text"] = num1 + num2
    else:
        lb["text"] = "Valores inválidos."

et1 = Entry(janela)
et1.place(x=100,y=100)

et2 = Entry(janela)
et2.place(x=100,y=130)

bt = Button(janela,text = "Soma", width = 20, command = bt_click)
bt.place(x=100,y=150)

lb = Label(janela,text = "Aguardando dados")
lb.place(x=100, y=200)

janela.geometry("400x300+200+200")
janela.mainloop()