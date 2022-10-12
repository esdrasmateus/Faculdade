carga_horaria = int(input("Informe a carga horária da sua disciplina (Em dias): "))
faltas = int(input("Informe a quantidade de faltas que você teve na disciplina (Em dias): "))
pnota = float(input("Informe a sua primeira nota: "))
snota = float(input("Informe a sua segunda nota: "))
media = (pnota + snota) / 2
porcentagem_faltas = faltas * 0.25
if pnota < 0 or pnota > 10 or snota < 0 or snota > 10:
    print("Suas notas precisam estar entre ou serem iguais a 0 e 10.")
elif porcentagem_faltas >= (carga_horaria * 0.25):
    print("Você está reprovado por faltas")
elif media >= 7 and porcentagem_faltas < (carga_horaria * 0.25):
    print("Você está aprovado.")
elif media >= 3 and media < 7 and porcentagem_faltas < (carga_horaria * 0.25):
    print("Você irá fazer a recuperação.")
elif media < 3:
    print("Você está reprovado por suas notas serem baixas.")