"""
int
float
str
bool

input

list
tuple
dict

if
else
elif
for
while
break
.format
:.2f
{}
[]
()
:

True
False

pass

and
or
not
is
>=
<=
range

def
args
kwargs

switch

OOP

let
var
const

ndwjdwiqjdksalncmzx = 12
"""
"""
int
float
str
bool

int = 489
float = 49.90
str = "dwuijdw" 'jdwijd'
bool = False


list

lista = [389, True, False, "dojsaiod", 0.39489]

lista[2] = 8

tuple

tupla = (1, 3, 5, 7)

tupla[1] = 6

dict

dicionario = { 1 : "alguma coisa", 2 : "alguma coisa", "hehe" : 8}

print(dicionario["alguma coisa"])
"""

"""while True:
    hehe = int(input("Digite seu numero de telefone: "))
    if (hehe == 0): 
        print(lista)
        break
    else:
        lista[3].append(hehe)"""


# Mariazinha quer comprar 10 bolas de gude e seus preços variam de acordo com o peso de cada uma
# Mariazinha tem 70 reais
# tabela de pesos:
# 1kg = 20 reais
# 2kg = 30 reais
# 1g = 2 reais
# Mariazinha gosta de coisas pesadas, entao ela quer no minimo uma bola de 1kg e 1 de 2kg
# Se a combinaçao de bolas de Mariazinha ultrapassar seu dinheiro, retorne que Mariazinha tem penis
# Se nao, retorne que Mariazinha tem bolas

listaDeBolas = {bola1G : 2, bola1KG : 20, bola2KG : 30}
totalGastoMariazinha = listaDeBolas[bola1KG] + listaDeBolas[bola2KG] + (listaDeBolas[bola1g] * 8)
# Variavel se Mariazinha nao tiver dinheiro:
#totalGastoMariazinha = listaDeBolas[bola1KG] + (listaDeBolas[bola2KG] * 9)

if (totalGastoMariazinha <= 70):
    print("Mariazinha tem bolas")
else:
    print("Mariazinha tem penis")

