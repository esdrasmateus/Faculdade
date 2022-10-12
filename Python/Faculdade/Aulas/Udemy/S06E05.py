p = float(input("Informe o peso total dos peixes em Kg: "))
e = int
m = int
if p > 50:
    e = (p - 50)
    m = (4 * e)
    print("O excesso de peixes é: {0:.2f} e a multa que deverá ser paga é {1:.2f}" .format(e,m))
else:
    print("Não há excesso de peixes")