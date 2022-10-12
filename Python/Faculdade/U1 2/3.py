x = int(input("Informe o primeiro número inteiro, positivo: "))
y = int(input("Informe o segundo número inteiro positivo: "))

if x >= y:
    while x != 0:
        z = x % y
        break
    print("O resto da divisão é {0}" .format(z))
elif y >= x:
    while y != 0:
        z = y % x
        break
    print("O resto da divisão é {0}" .format(z))