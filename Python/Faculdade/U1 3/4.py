frase = input('Digite uma frase: ')

vogal_a = 0
vogal_e = 0
vogal_o = 0
vogal_i = 0
vogal_u = 0
digito_1 = 0
digito_2 = 0
digito_3 = 0
digito_4 = 0
digito_5 = 0
digito_6 = 0
digito_7 = 0
digito_8 = 0
digito_9 = 0
digito_0 = 0

for i in range(len(frase)):
  if frase[i] == 'a':
    vogal_a += 1
  elif frase[i] == 'e':
    vogal_e += 1
  elif frase[i] == 'i':
    vogal_i += 1
  elif frase[i] == 'o':
    vogal_o += 1
  elif frase[i] == 'u':
    vogal_u += 1
  elif frase[i] == '1':
    digito_1 += 1
  elif frase[i] == '2':
    digito_2 += 1
  elif frase[i] == '3':
    digito_3 += 1
  elif frase[i] == '4':
    digito_4 += 1
  elif frase[i] == '5':
    digito_5 += 1
  elif frase[i] == '6':
    digito_6 += 1
  elif frase[i] == '7':
    digito_7 += 1
  elif frase[i] == '8':
    digito_8 += 1
  elif frase[i] == '9':
    digito_9 += 1
  elif frase[i] == '0':
    digito_0 += 1

vogais = {'a' : vogal_a, 'e' : vogal_e, 'i' : vogal_i, 'o' : vogal_o, 'u' : vogal_u}
numeros = {0 : digito_0, 1 : digito_1, 2 : digito_2, 3 : digito_3, 4 : digito_4, 5 : digito_5, 6 : digito_6, 7 : digito_7, 8 : digito_8, 9 : digito_9}

print("O número de vogais é {0} e o número de dígitos {1}" .format(vogais,numeros))