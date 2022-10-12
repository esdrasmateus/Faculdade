altura = float(input("Informe a altura do reservatório em centímetros: "))
largura = float(input("Informe a largura do reservatório em centímetros: "))
comprimento = float(input("Informe o comprimento do reservatório em centímetros: "))
consumo_diario = float(input("Informe o consumo médio diário de água em litros: "))
volume = (altura * largura * comprimento)
capacidade_litros = volume / 1000
autonomia = capacidade_litros / consumo_diario
dias_consumo = capacidade_litros / consumo_diario
if dias_consumo < 2:
    print("A capacidade do reservatório é de: {0:.2f}, a autonomia do reservatório é de {1:.2f} e o consumo é classificado em elevado." .format(capacidade_litros,autonomia))
elif dias_consumo >= 2 and dias_consumo <= 7:
    print("A capacidade do reservatório é de: {0:.2f}, a autonomia do reservatório é de {1:.2f} e o consumo é classificado em moderado." .format(capacidade_litros,autonomia))
elif dias_consumo > 7:
    print("A capacidade do reservatório é de: {0:.2f}, a autonomia do reservatório é de {1:.2f} e o consumo é classificado em reduzido." .format(capacidade_litros,autonomia))