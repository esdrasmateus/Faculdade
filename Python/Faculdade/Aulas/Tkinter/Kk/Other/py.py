from tkinter import *

janela1 = Tk()

lista1 = ["@everyone"]

def chamar_cornos():
    if entry1.get() in lista1:
        print("@Ito @Bia Among @Léo @Roi Malu Né? @Mirella @Arthur @Thiago @Larissa")
        exit()
    else:
        exit()

label1 = Label(janela1, text = "Digite @everyone para chamar todos os cornos")
label1.grid(row = 0, column = 0)

entry1 = Entry(janela1)
entry1.grid(row = 0, column = 1)

button1 = Button(janela1, width = 20, command = chamar_cornos)
button1.grid(row = 1, column = 0)

janela1.mainloop()