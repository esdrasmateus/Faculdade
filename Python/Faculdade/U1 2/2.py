print("Calculo de altura para Zé e Chico")
chico = 1.50
ze = 1.10
i1 = 0.2
i2 = 0.3
anos = 0

while ze < chico:
    chico += i1
    ze += i2
    anos += 1
print("A quantidade de anos necessários para Zé ser maior que Chico é {0}".format(anos))