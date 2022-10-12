import random

x = 0

lista1 = []

while x < 180:

    char1 = ["D","B","P"] #primeiro caractere da palavra

    char2 = ["V","X","Y"] #segundo caractere da palavra

    char3 = ["5","7"] #terceiro caractere da palavra

    char4 = ["2","3","8","9","0"] #quarto caractere da palavra

    char5 = ["5","7"] #quinto caractere da palavra

    #escolher um caractere aleatorio das listas anteriores
    var1 = random.choice(char1)
    var2 = random.choice(char2)
    var3 = random.choice(char3)
    var4 = random.choice(char4)
    var5 = random.choice(char5)
    
    #concatenando as strings anteriores
    varall1 = var1 + var2 + var3 + var4 + var5
    
    #if para a primeira situação
    if x == 0:
        print("L" + varall1 + "6")
        lista1.append(varall1)
        x += 1
    #if para nao ter repetição
    if varall1 not in lista1:
        print("L" + varall1 + "6")
        lista1.append(varall1)
        x += 1
        
#lista ordenada
print(sorted(lista1))

#numero de resultados da lista para ter certeza que não tem repetição
lenght = len(lista1)

print(lenght)