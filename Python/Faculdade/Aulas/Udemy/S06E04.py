altura = float(input("Informe a sua altura: "))
sexo = input("Qual é o seu sexo? (m para masculino, f para feminino): ")
if sexo.lower() == 'f':
    peso_ideal = (62.1 * altura) - 44.7
elif sexo.lower() == 'm':
    peso_ideal = (72.7 * altura) - 58.0
else:
    peso_ideal = 0
    print("Informe o sexo com uma variável compatível")
print("O seu peso ideal é {0:.2f}" .format(peso_ideal))