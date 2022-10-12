maior = -999
menor = 999
soma = 0

for n in range (1,11):
    valor = int(input("Informe um valor: "))
    if valor > 0:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
        soma = soma + valor
    else:
        valor = int(input("Informe um valor: "))
media = (soma / 10)

print("O maior valor é: {0}" .format(maior))
print("O menor valor é: {0}" .format(menor))
print("A média é: {0}" .format(media))