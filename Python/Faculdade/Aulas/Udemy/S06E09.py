poluiçao = float(input("Informe o índice de poluição: "))
if poluiçao >= 0.3 and poluiçao < 0.4:
    print("O grupo 1 precisa suspender as atividades")
elif poluiçao >= 0.4 and poluiçao < 0.5:
    print("Os grupos 1 e 2 precisam suspender as atividades")
elif poluiçao >= 0.5:
    print("Todos os grupos precisam suspender as atividades")
else:
    print("Níveis aceitáveis")