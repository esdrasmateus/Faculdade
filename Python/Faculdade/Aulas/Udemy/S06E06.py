c = input("Informe o código do operário: ")
numero_horas = float(input("Informe o número de horas trabalhadas: "))
salário = float
if numero_horas <= 50:
    salário = 10 * numero_horas
    print("O seu salário é : {0}" .format(salário))
else:
    salário = 20 * numero_horas
    print("Horas extras! O seu salário é : {0}" .format(salário))