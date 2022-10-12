"""
Ranges

- Necessários para entender loops
- São usados como auxiliadores para os loops
- A função range é utilizada para sequências numéricas de maneiras específicas

Exemplo:

for variavel in range(y):
    funçao(variavel)

for n in range(12):  *aqui n será printado 11 vezes, pois a funçao range usa o número final-1
    print(n)

- A função range também pode ter seu valor de início específicado pelo usuário

Exemplo:

for variavel in range(x,y):
    funçao(variavel)

for n in range(5,11):   *aqui n será printado 6 vezes
    print(n)

- Também é possível que seja determinado o "passo" do range, que é como ele contará
   a quantidade de números

Exemplo:

for variavel in range(x,y,z):
    print(variavel)

for n in range(1,11,2): *aqui n será repetido 5 vezes, pois o terminal irá retornar
                          o valor de dois em dois na lista
    print(n)

"""
