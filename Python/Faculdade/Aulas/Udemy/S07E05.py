usuário = input("Informe um nome de usuário: ")
senha = input("Informe uma senha: ")

while senha == usuário:
    print("Sua senha não pode ser igual ao seu nome de usuário.")
    print("Informe um nome de usuário")
    usuário = input()
    print("Informe uma senha")
    senha = input()
print("Informações aceitas")