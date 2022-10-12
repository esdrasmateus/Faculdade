quantidade = 0
necessita_esfera = 0
necessita_limpeza = 0
necessita_troca_cabo = 0
quebrado = 0
identificação = int(input("Informe a identificação: "))
while identificação != 0:
    print("Digite 1 para mouses que: necessitam de esfera")
    print("Digite 2 para mouses que: necessitam de limpeza")
    print("Digite 3 para mouses que: necessitam trocar o cabo")
    print("Digite 4 para mouses que: estiverem quebrados")
    defeito = int(input("Identifique o defeito: "))
    if defeito == 1:
        necessita_esfera = necessita_esfera + 1
    elif defeito == 2:
        necessita_limpeza = necessita_limpeza + 1
    elif defeito == 3:
        necessita_troca_cabo = necessita_troca_cabo+ 1
    elif defeito == 4:
        quebrado = quebrado + 1
    quantidade = quantidade + 1
    identificação = int(input("Informe a identificação: "))
perc_esfera = (necessita_esfera * 100.0) /quantidade
perc_limpeza = (necessita_limpeza * 100.0) /quantidade
perc_cabo = (necessita_troca_cabo * 100.0) /quantidade
perc_quebrado = (quebrado * 100.0) /quantidade

print("A quantidade de mouses é: {0}" .format(quantidade))
print("Situação                                      Quantidade    Percentual")
print("1 = Necessita da esfera                          {0}          {1:.2f}%" .format(necessita_esfera,perc_esfera))
print("2 = Necessita de limpeza                         {0}          {1:.2f}%" .format(necessita_limpeza,perc_limpeza))
print("3 = Necessita troca do cabo ou conector          {0}          {1:.2f}%" .format(necessita_troca_cabo,perc_cabo))
print("4 = Quebrado ou inutilizado                      {0}          {1:.2f}%" .format(quebrado,perc_quebrado))