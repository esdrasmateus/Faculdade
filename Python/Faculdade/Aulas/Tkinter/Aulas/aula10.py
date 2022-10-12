from tkinter import *

janela = Tk()

lb1 = Label(janela , text = "Label1", bg="green")


lb2 = Label(janela , text = "Label2", bg="red")


lb3 = Label(janela , text = "Label3", bg="blue")


lb4 = Label(janela , text = "Label4", bg="purple")

lb1.pack(side=RIGHT)
lb2.pack(side=TOP)
lb3.pack(side=LEFT)
lb4.pack(side=BOTTOM)

janela["bg"] = "black"

janela.geometry("400x300+200+200")
janela.mainloop()