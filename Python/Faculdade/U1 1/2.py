moeda_desejada = (input("Informe a moeda a ser convertida: "))
valor_reais = float(input("Informe a quantidade em reais a ser convertida: "))
valor_convertido = 0
e = 0.31
d = 0.42
m = 5.55
a = 2.84
l = 0.26
if moeda_desejada.lower() == 'e':
    valor_convertido = (valor_reais * e)
    print("O valor convertido a ser devolvido é: {0:.2f}" .format(valor_convertido))
elif moeda_desejada.lower() == 'd':
    valor_convertido = (valor_reais * d)
    print("O valor convertido a ser devolvido é: {0:.2f}" .format(valor_convertido))
elif moeda_desejada.lower() == 'm':
    valor_convertido = (valor_reais * m)
    print("O valor convertido a ser devolvido é: {0:.2f}" .format(valor_convertido))
elif moeda_desejada.lower() == 'a':
    valor_convertido = (valor_reais * a)
    print("O valor convertido a ser devolvido é: {0:.2f}" .format(valor_convertido))
elif moeda_desejada.lower() == 'l':
    valor_convertido = (valor_reais * l)
    print("O valor convertido a ser devolvido é: {0:.2f}" .format(valor_convertido))
else:
    print("Digite uma moeda válida")