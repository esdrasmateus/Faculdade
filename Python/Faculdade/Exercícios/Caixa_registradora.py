total_produto_501 = 0
total_produto_502 = 0
total_produto_503 = 0
total_produto_504 = 0
total_produto_505 = 0
total_produto_506 = 0

codigo = int(input("Digite o código do produto: "))
while codigo != 0:
    if codigo == 501:
        total_produto_501 = total_produto_501 + 1
    elif codigo == 502:
        total_produto_502 = total_produto_502 + 1
    elif codigo == 503:
        total_produto_503 = total_produto_503 + 1
    elif codigo == 504:
        total_produto_504 = total_produto_504 + 1
    elif codigo == 505:
        total_produto_505 = total_produto_505 + 1
    elif codigo == 506:
        total_produto_506 = total_produto_506 + 1
    else:
        print("Digite um código válido.")
    codigo = int(input("Digite o código do produto: "))


dinheiro501 = (total_produto_501 * 7.95)
dinheiro502 = (total_produto_502 * 4.65)
dinheiro503 = (total_produto_503 * 9.85)
dinheiro504 = (total_produto_504 * 9.85)
dinheiro505 = (total_produto_505 * 29.90)
dinheiro506 = (total_produto_506 * 5.95)
quantia_total = (dinheiro501 + dinheiro502 + dinheiro503 + dinheiro504 + dinheiro505 + dinheiro506)

print("O valor total da sua compra é: {0:.2f} " .format(quantia_total))
       