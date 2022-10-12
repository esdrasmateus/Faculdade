""" for item in interavel:
    loop

- String
    string = "My string"
- List
    array = [1, 3, 4, 5, 6]
- Range
    numbers = range(1, 10)


# Exemplo de for 1

for letra in name:
    print(letra)

# Exemplo 2

for number in lista:
    print(number)

# Exemplo 3

for number in numbers:
    print(number)

for i, v in enumerate(name):
    print(name[i]) 
    
for _, letra in enumerate(name):
    print(letra)
    
for valor in enumerate(name):
    print(valor[0])
    
name = "My string"
lista = [1, 3, 4, 6, 8]
numbers = range(1, 11)

qtd = int(input("How many times you want the loop to execute? "))
_sum = 0;

for n in range(1, qtd + 1):
    num = int(input(f"Informe o {n}/{qtd} valor: "))
    _sum += num;
print(f"A soma é {_sum}")

nome = "My string"
for letra in nome:
    print(letra, end='')"""