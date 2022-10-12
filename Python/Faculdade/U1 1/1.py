valor_casa = float(input("Informe o valor da casa a comprar: "))
salario = float(input("Informe o seu salário: "))
anos_a_pagar = int(input("Informe em quantos anos a casa será paga: "))

meses = (anos_a_pagar * 12)
prestaçao_mensal = (valor_casa / meses)
porcentagem_salario = (salario * 0.30)

if prestaçao_mensal > porcentagem_salario:
    print("O seu salário ({0:.2f}) é menor do que 30 por cento da prestação mensal ({1:.2f}), por isso o seu empréstimo foi recusado.".format(salario,prestaçao_mensal))
elif prestaçao_mensal == porcentagem_salario:
    print("O seu salário ({0:.2f}) é igual a 30 por cento da prestação mensal ({1:.2f}), por isso o seu empréstimo foi aprovado.".format(salario,prestaçao_mensal))
else:
    print("O seu salário ({0:.2f}) é maior do que 30 por cento da prestação mensal ({1:.2f}), por isso o seu empréstimo foi aprovado.".format(salario,prestaçao_mensal))