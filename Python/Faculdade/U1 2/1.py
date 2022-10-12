print("Calculo da soma dos n primeiros inteiros positivos")
n = int(input("Digite o valor de n: "))
soma = 0
i = 1
while i <= n:
    soma += i
    i += + 1
quadrado_da_soma = (soma * soma)
print("A soma dos {0} primeiros números inteiros positivos é {1} e o quadrado da sua soma é {2}" .format(n,soma,quadrado_da_soma))
soma2 = 0
i2 = 1
while i2 <= n:
    soma2 += i2 * i2
    i2 += 1
print("A soma dos quadrados dos {0} primeiros números inteiros positivos é {1}." .format(n,soma2))