linhas = 0
alunos = []
matriculas_e_medias = []
medias = []
while linhas < 5:
    matricula = int(input("Digite o número da matrícula: "))
    nota1 = float(input("Digite a média das provas: "))
    if nota1 > 10 or nota1 < 0:
        print("Sua nota precisa ser igual ou estar entre 0 e 10")
        continue
    nota2 = float(input("Digite a média dos trabalhos: "))
    if nota2 > 10 or nota1 < 0:
        print("Sua nota precisa ser igual ou estar entre 0 e 10")
        continue
    media = (nota1 + nota2) / 2
    alunos.append([matricula, nota1, nota2, media])
    matriculas_e_medias.append([media, matricula])
    medias.append(media)
    linhas += 1
print(alunos)
print("A nota mais alta e a matricula do aluno, respectivamente foram {0}" .format(max(matriculas_e_medias)))
soma_das_notas = sum(medias) / 5
print("A média aritmética das notas é {0}" .format(soma_das_notas))