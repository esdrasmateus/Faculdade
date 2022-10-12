número = int(input("Informe um número: "))
if (número % 2 == 0) and número > 0:
    print("O número é positivo e par")
elif (número % 2 == 0) and número < 0:
    print("O número é negativo e par")
elif (número % 2 != 0) and número > 0:
    print("O número é positivo e ímpar")
elif (número % 2 != 0) and número < 0:
    print("O número é negativo e ímpar")
else:
    pass