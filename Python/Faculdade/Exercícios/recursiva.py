def fat(n):
    resultado = 0
    while n > 0:
        resultado = resultado + n
        n = n - 1
    return resultado
print("A soma é de: {0}" .format(fat(int(input("Digite uma variável: ")))))