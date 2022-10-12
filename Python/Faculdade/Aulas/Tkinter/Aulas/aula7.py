from tkinter import *
from functools import partial
""" Duas funções para dois botões
def button_click_1():
    print("Clickou no 1 :)")

def button_click_2():
    print("Clickou no 2 :)")
"""

def bt_click(botao):
    print(botao["text"])

janela = Tk()

bt1 = Button(janela,width=20, text="Button 1")
bt1["command"] = partial(bt_click, bt1)
bt1.place(x=100,y=100)

bt2 = Button(janela,width=20,text = "Button 2")
bt2["command"] = partial(bt_click, bt2)
bt2.place(x=100,y=130)

janela.geometry("300x300+200+200")
janela.mainloop()