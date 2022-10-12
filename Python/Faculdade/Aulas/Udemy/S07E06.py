x = int(input("Informe um número: "))
i = int
valor = int
while x < 1 or x > 10:
    print("O número precisa ser menor ou igual a 10 e maior que 0")
    x = int(input("Informe um número: "))
print("Tabuada de {0}: " .format(x))
for i in range(1,11):
    valor = x * i
    print("{0} x {1} = {2}" .format(x,i,valor))