n = int(input("Informe um número positivo e inteiro: "))

fib1 = 0
fib2 = 1

print("0")
print("1")

while fib2 <= n:
    fibn = fib1 + fib2
    print("{0}" .format(fibn))
    fib1 = fib2
    fib2 = fibn