from tkinter import *

import random

janela1 = Tk()

label1 = Label(janela1, text = "Digite 0 para papel, 1 para pedra e 2 para tesoura")
label1.grid(row = 0, column = 0)

label2 = Label(janela1, text = "")
label2.grid(row = 3, column = 0)

entry1 = Entry(janela1)
entry1.grid(row = 1, column = 1)

label3 = Label(janela1,text = "")
label3.grid(row = 4, column = 0)

def compplay():
    variavelplayer = str
    if entry1.get() == 1:
        variavelplayer = 1
        variavelplayer2 = variavelplayer
    elif entry1.get() == 0:
        variavelplayer = 0
        variavelplayer2 = variavelplayer
    elif entry1.get() == 2:
        variavelplayer = 2
        variavelplayer2 = variavelplayer
    else:
        label3["text"] = "Digite um número válido"
    variavelcomp = random.getrandbits(2)
    print(variavelplayer2)
    if variavelcomp == 0:
        label2["text"] = ("O computador jogou pedra")
        variavelcomp = 0

    elif variavelcomp == 1:
        label2["text"] = ("O computador jogou papel")
        variavelcomp = 1
    else:
        label2["text"] = ("O computador jogou tesoura")
        variavelcomp = 2

    if variavelcomp == variavelplayer:
        label3["text"] = "Empate"
    elif variavelcomp == 0 and variavelplayer == 1:
        label3["text"] = "Você perdeu! :("
    elif variavelcomp == 1 and variavelplayer == 0:
        label3["text"] = "Você ganhou! :)"
    elif variavelcomp == 0 and variavelplayer == 2:
        label3["text"] = "Você perdeu! :("
    elif variavelcomp == 1 and variavelplayer == 2:
        label3["text"] = "Você perdeu! :("
    elif variavelcomp == 2 and variavelplayer == 1:
        label3["text"] = "Você ganhou! :)"
    elif variavelcomp == 2 and variavelplayer == 0:
        label3["text"] = "Você ganhou! :)"

button1 = Button(janela1, width = 20, text = "Jogar", command = compplay)
button1.grid(row = 1, column = 2)

janela1.mainloop()