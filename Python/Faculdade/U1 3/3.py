camisa1 = 0
camisa2 = 0
camisa3 = 0
camisa4 = 0
camisa5 = 0
camisa6 = 0
camisa7 = 0
camisa8 = 0
camisa9 = 0
camisa10 = 0
camisa11 = 0
camisa12 = 0
camisa13 = 0
camisa14 = 0
camisa15 = 0
camisa16 = 0
camisa17 = 0
camisa18 = 0
camisa19 = 0
camisa20 = 0
camisa21 = 0
camisa22 = 0
camisa23 = 0
quantidade = 0

identificação = int(input("Informe a camisa do jogador: "))
while identificação != 0:
    numero_da_camisa = identificação
    if numero_da_camisa < 0 or numero_da_camisa > 23:
        print("O número da camisa precisa estar entre ou ser igual a 1 e 23")
    elif numero_da_camisa == 1:
        camisa1 += 1
    elif numero_da_camisa == 2:
        camisa2 += 1
    elif numero_da_camisa == 3:
        camisa3 += 1
    elif numero_da_camisa == 4:
        camisa4 += 1
    elif numero_da_camisa == 5:
        camisa5 += 1
    elif numero_da_camisa == 6:
        camisa6 += 1
    elif numero_da_camisa == 7:
        camisa7 += 1
    elif numero_da_camisa == 8:
        camisa8 += 1
    elif numero_da_camisa == 9:
        camisa9 += 1
    elif numero_da_camisa == 10:
        camisa10 += 1
    elif numero_da_camisa == 11:
        camisa11 += 1
    elif numero_da_camisa == 12:
        camisa12 += 1
    elif numero_da_camisa == 13:
        camisa13 += 1
    elif numero_da_camisa == 14:
        camisa14 += 1
    elif numero_da_camisa == 15:
        camisa15 += 1
    elif numero_da_camisa == 16:
        camisa16 += 1
    elif numero_da_camisa == 17:
        camisa17 += 1
    elif numero_da_camisa == 18:
        camisa18 += 1
    elif numero_da_camisa == 19:
        camisa19 += 1
    elif numero_da_camisa == 20:
        camisa20 += 1
    elif numero_da_camisa == 21:
        camisa21 += 1
    elif numero_da_camisa == 22:
        camisa22 += 1
    elif numero_da_camisa == 23:
        camisa23 += 1
    quantidade += 1
    identificação = int(input("Informe a camisa do jogador (Digite 0 para sair): "))

perc_1 = (camisa1 * 100.0) /quantidade
perc_2 = (camisa2 * 100.0) /quantidade
perc_3 = (camisa3 * 100.0) /quantidade
perc_4 = (camisa4 * 100.0) /quantidade
perc_5 = (camisa5 * 100.0) /quantidade
perc_6 = (camisa6 * 100.0) /quantidade
perc_7 = (camisa7 * 100.0) /quantidade
perc_8 = (camisa8 * 100.0) /quantidade
perc_9 = (camisa9 * 100.0) /quantidade
perc_10 = (camisa10 * 100.0) /quantidade
perc_11 = (camisa11 * 100.0) /quantidade
perc_12 = (camisa12 * 100.0) /quantidade
perc_13 = (camisa13 * 100.0) /quantidade
perc_14 = (camisa14 * 100.0) /quantidade
perc_15 = (camisa15 * 100.0) /quantidade
perc_16 = (camisa16 * 100.0) /quantidade
perc_17 = (camisa17 * 100.0) /quantidade
perc_18 = (camisa18 * 100.0) /quantidade
perc_19 = (camisa19 * 100.0) /quantidade
perc_20 = (camisa20 * 100.0) /quantidade
perc_21 = (camisa21 * 100.0) /quantidade
perc_22 = (camisa22 * 100.0) /quantidade
perc_23 = (camisa23 * 100.0) /quantidade

lista1 = [camisa1, camisa2, camisa3, camisa4, camisa5, camisa6, camisa7, camisa8, camisa9, camisa10, camisa11, camisa12, camisa13, camisa14, camisa15, camisa16, camisa17, camisa18, camisa19, camisa20, camisa21, camisa22, camisa23]
maior_numero_lista1 = max(lista1)
lista2 = [perc_1, perc_2, perc_3, perc_4, perc_5, perc_6, perc_7, perc_8, perc_9, perc_10, perc_11, perc_12, perc_13, perc_14, perc_15, perc_16, perc_17, perc_18, perc_19, perc_20, perc_21, perc_22, perc_23]
maior_porcentagem = max(lista2)
print("A quantidade votos é: {0}" .format(quantidade))
print("Camisa                                  Quantidade de votos    Percentual")
print("1                                                 {0}            {1:.2f}%" .format(camisa1,perc_1))
print("2                                                 {0}            {1:.2f}%" .format(camisa2,perc_2))
print("3                                                 {0}            {1:.2f}%" .format(camisa3,perc_3))
print("4                                                 {0}            {1:.2f}%" .format(camisa4,perc_4))
print("5                                                 {0}            {1:.2f}%" .format(camisa5,perc_5))
print("6                                                 {0}            {1:.2f}%" .format(camisa6,perc_6))
print("7                                                 {0}            {1:.2f}%" .format(camisa7,perc_7))
print("8                                                 {0}            {1:.2f}%" .format(camisa8,perc_8))
print("9                                                 {0}            {1:.2f}%" .format(camisa9,perc_9))
print("10                                                {0}            {1:.2f}%" .format(camisa10,perc_10))
print("11                                                {0}            {1:.2f}%" .format(camisa11,perc_11))
print("12                                                {0}            {1:.2f}%" .format(camisa12,perc_12))
print("13                                                {0}            {1:.2f}%" .format(camisa13,perc_13))
print("14                                                {0}            {1:.2f}%" .format(camisa14,perc_14))
print("15                                                {0}            {1:.2f}%" .format(camisa15,perc_15))
print("16                                                {0}            {1:.2f}%" .format(camisa16,perc_16))
print("17                                                {0}            {1:.2f}%" .format(camisa17,perc_17))
print("18                                                {0}            {1:.2f}%" .format(camisa18,perc_18))
print("19                                                {0}            {1:.2f}%" .format(camisa19,perc_19))
print("20                                                {0}            {1:.2f}%" .format(camisa20,perc_20))
print("21                                                {0}            {1:.2f}%" .format(camisa21,perc_21))
print("22                                                {0}            {1:.2f}%" .format(camisa22,perc_22))
print("23                                                {0}            {1:.2f}%" .format(camisa23,perc_23))

print("O melhor jogador da partida foi {0}, com um total de votos de {1}, correspondendo a {2:.2f}% dos votos" .format(max(lista1),quantidade,max(lista2)))