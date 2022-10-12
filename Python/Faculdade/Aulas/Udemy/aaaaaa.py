valor1 = int(input(("Digite o primeiro valor de entrada: ")))

valor2 = int(input("Digite o segundo valor de entrada: "))

for i in range(valor1, valor2):
    if i % 2 == 0:
        print("{0}".format(i))