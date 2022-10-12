from tkinter import *

janela = Tk()

lb1 = Label(janela, text = "Label1")
lb1.grid(row = 10, column = 10)

janela.geometry("500x200+600+200")
janela.mainloop()