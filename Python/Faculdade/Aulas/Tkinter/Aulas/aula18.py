from tkinter import *

janela = Tk()


lb1 = Label(janela, text = "ESPAÇO", width = "15", height = 3, bg = "blue")
lbHorizontal = Label(janela, text = "Horizontal", bg = "yellow")
lbVertical = Label(janela, text = "Vertical")

lb1.grid(row = 0, column = 0)
lbHorizontal.grid(row = 1, column = 0, sticky = W)

janela.geometry("")
janela.mainloop()