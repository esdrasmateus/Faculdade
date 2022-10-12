""" lista1 = [1,2,3,4,5,6,7]

if 8 in lista1:
    print(8)
else:
    print(9) """

""" lista1 = [3,4,5,6]
lista2 = lista1.copy()

lista1.append(5)

print(lista2) """

""" s = set({1, 2, 3, 4, 5, 2, 3})
print(type(s)) """

""" s = {1, 2, 3, 4, 5, 6, 2, 3}
print(s)
print(type(s))

from collections import Counter

lista = [1,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,1,1,1,1,1,1,2,2,2,2,2,2,4,5,6,1,2,3,4,5,6]

res = Counter(lista)

print(res)

print(Counter("Hehehehehehehhejajajajajaiqkwncuiasjdwijqiwhudewknm,a")) 

from collections import defaultdict, OrderedDict

dictio = defaultdict(lambda: 0)
dictio["curso"] = "Hehe"
dictio["a"] = "a"

dictio2 = OrderedDict(dictio)
print(dictio2) 

from collections import namedtuple

tupla1 = namedtuple("tupla1", "dede" "dada")

# ou

tupla2 = namedtuple("tupla2", "dede, dada")

# ou

tupla3 = namedtuple("tupla3", ["dede", "dada"])

haha = tupla1(dede = "hehe1", dada = "hehe2")
print(haha[0]) 

from collections import deque

deq = deque("haha")

deq.appendleft("hehe")

print(deq)

numeros = [1,2,3,4,5]
res = [numero * 10 for numero in numeros]
print(res)"""