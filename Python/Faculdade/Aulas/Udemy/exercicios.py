""" A = [1, 0, 5, -2, -5, 7]

print(A[0] + A[1] + A[5])

A[4] = 100
print(*A, sep = "\n") """

""" b = []

for i in range(1, 7):
    a = int(input("Digite um valor: "));
    b.append(a)
    i += 1

print(b) """

""" b = []
for i in range(1,11):
    a = int(input("Digite um valor: "))
    a *= a
    b.append(a)
    i += 1

print(b) """

""" b = []
for i in range(1, 9):
    a = int(input("Digite um valor: "))
    b.append(a)

c = int(input("Digite a primeira posiçao para somar no vetor: "))
d = int(input("Digite a segunda posiçao para somar no vetor: "))

print(b[c] + b[d]) """

def duplicar(num = 1):
    return num * 2
