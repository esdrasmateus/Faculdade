idade = int(input("Informe a idade do nadador: "))
if idade >= 5 and idade <= 7:
    print("O nadador é infantil 'A'")
elif idade >= 8 and idade <= 11:
    print("O nadador é infantil 'B'")
elif idade >= 12 and idade <= 13:
    print("O nadador é juvenil 'A'")
elif idade >= 14 and idade <= 17:
    print("O nadador é juvenil 'B'")
elif idade >=18:
    print("O nadador é adulto")
else:
    print("O nadador precisa ter no mínimo 5 anos")