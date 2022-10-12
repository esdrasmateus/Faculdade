import database

class Person:
    def __init__(self, name, age, email, phone, address, username, password):
        
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.address = address
        self.username = username
        self.password = password

class Book:
    def __init__(self, title, author, tag, stock, number):

        self.number = number
        self.title = title
        self.author = author
        self.tag = tag
        self.stock = stock

def Register():

    contains = ["@", "."]

    name = str(input("Nome: "))
    age = int(input("Idade: "))
    email = str(input("Email: "))

    if all(x not in email for x in contains):
        email = str(input("Insira um email válido: "))

    phone = int(input("Telefone (Sem espaços ou caracteres especiais): "))

    if len(str(phone)) < 8:
        phone = int(input("Insira um número de telefone válido: "))

    address = str(input("Endereço: "))
    username = str(input("Usuário: "))
    password = str(input("Senha: "))

    user = Person(name, age, email, phone, address, username, password)
    database.CreateEntry(user)

loginInput = int(input("Olá, seja bem vindo à biblioteca Folha. Se já tiver um cadastro, digite '1' para entrar e escolher um livro, se não, digite qualquer outro número para registrar-se\n"))

if (loginInput == 1):
    while True:

        print("Digite seus dados para entrar no sistema")
        username = str(input("Usuário: "))
        password = str(input("Senha: "))
        user = database.SearchEntry(username, password)
        if (user == True):
            print("Login com sucesso")
            break
        else:
            print("Usuário ou senha incorretos!")
            loop = int(input("Digite 1 para tentar novamente ou 2 para sair: "))
            if (loop == 2): exit()

else: Register()

bookArray = []
bookQuantity = database.SearchMany()

if bookQuantity == 0:
    book1 = Book("A Seleção","Kiera Cass","Romance", 5, 1)
    book2 = Book("Corte de Espinhos e Rosas","Sarah J. Maas","Romance", 3, 2)
    book3 = Book("Os Miseráveis","Victor Hugo","Romance", 8, 3)
    book4 = Book("Drácula","Bram Stoker","Terror", 2, 4)
    book5 = Book("It-A Coisa","Stephen King","Terror", 1, 5)
    book6 = Book("O Chamado de Cthulhu","H. P. Lovecraft","Terror", 8, 6)
    book7 = Book("Jogos Vorazes","Suzanne Collins","Ação", 4, 7)
    book8 = Book("A Guerra dos Tronos -- As Crônicas de Gelo e Fogo","George R. R. Martin","Ação", 12, 8)
    book9 = Book("Percy Jackson e os Olimpianos -- O Ladrão de Raios","Rick Riordan","Ação", 6, 9)
    book10 = Book("Dom Casmurro","Machado de Assis","Clássico", 2, 10)
    book11 = Book("O Cortiço","Aluísio Azevedo","Clássico", 5, 11)
    book12 = Book("Hamlet","William Shakespeare","Clássico", 1, 12)

    bookArray = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10, book11, book12]
    bookLen = len(bookArray)
    i = 0
    while i < bookLen: 
        database.CreateBook(bookArray[i])
        i += 1

else:
    i = 0
    while i < bookQuantity:
        updater = database.SearchBook(i + 1)
        bookUpdater = Book(updater["title"], updater["author"], updater["tag"], updater["stock"], updater["Book ID"])
        bookArray.append(bookUpdater)
        i += 1

bookLen = len(bookArray)

def MainMenu():
    print("A lista de livros desta biblioteca é: ")
    i = 0
    while i < (bookLen):
        print("ID: {0}      Título: {1}      Autor(a): {2}    Classificação: {3}    Quantidade Disponível: {4}\n".format(bookArray[i].number, bookArray[i].title, bookArray[i].author, bookArray[i].tag, bookArray[i].stock))
        i += 1

    return int(
        input(
            "Se quiser escolher um livro, digite 1\nSe quiser ver a sua lista de livros escolhidos, digite 2\nSe quiser devolver um livro, digite 3\nDigite qualquer outro número se quiser encerrar sua seção\n"
        )
    )

choose = MainMenu()
chosenBooks = []

while (choose > 0) and (choose < 4):
    if (choose == 1):
        chooseBook = int(input("Digite o ID do livro que deseja alugar: "))
        while (chooseBook < 1) or (chooseBook > database.SearchMany()):
            chooseBook = int(input("Digite um ID válido: "))

        chosenBook = bookArray[chooseBook - 1]

        if (chosenBook.stock <= 0):
            back = int(input("Infelizmente, esse livro não está disponível no nosso estoque."))
            choose = MainMenu()
        else:
            database.TakeBook(chosenBook)
            chosenBooks.append(chosenBook)

            choose = MainMenu()

    elif choose == 2:
        chosenLen = len(chosenBooks)
        if chosenLen <= 0:
            print("Você não tem nenhum livro na sua lista")
            wantChoose = int(input("Se quiser começar a escolher livros, digite 1\nDigite qualquer outro número se deseja voltar ao menu inicial: "))
            choose = 1 if (wantChoose == 1) else MainMenu()
        else:
            print("Os livros escolhidos foram: ")
            i = 0
            while i < chosenLen:
                print("ID: {0}      Título: {1}      Autor(a): {2}    Classificação: {3}    Quantidade Disponível na biblioteca: {4}\n".format(chosenBooks[i].number, chosenBooks[i].title, chosenBooks[i].author, chosenBooks[i].tag, chosenBooks[i].stock))
                i += 1

            choose = MainMenu()

    elif (choose == 3):
        bookName = str(input("Digite o título do livro: "))
        bookAuthor = str(input("Digite o autor do livro: "))
        bookTag = str(input("Digite a classificação do livro: "))
        bookStock = int(input("Digite quantos desse livro você irá devolver: "))

        newBook = Book(bookName, bookAuthor, bookTag, bookStock, bookLen + 1)
        database.CreateBook(newBook)

        bookArray.append(newBook)
        bookLen = len(bookArray)

        print("Seu livro foi adicionado ao sistema!")
        choose = MainMenu()

    else: exit()