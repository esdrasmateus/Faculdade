import tkinter as tk

#Definindo variável
janela = tk.Tk()

#Mudando título
janela.title("Janela principal")

#Mudando background
janela ["bg"] = "green"
janela ["background"] = "green"

#Largura x altura, e quanto pra esquerda ou topo da tela a janela vai aparecer

janela.geometry("800x300+100+100")

#O que vier depois disso no código só vai ser executado após a janela fechar
janela.mainloop()