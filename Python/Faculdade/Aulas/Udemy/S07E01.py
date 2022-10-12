n = int(input("Informe um número: "))
maior = 0
while n != 0:
    if n > maior:
        maior = n
    n = int(input("Informe um número(Para parar o looping informe 0): "))
print("O maior número é {0}" .format(maior))