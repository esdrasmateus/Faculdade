# Parent Class

class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_details(self):
        print(f"Personal details\n\nName: {self.name}\nAge: {self.age}\nGender: {self.gender}")

hehe = User("Hehe", 21, "Male")

hehe.show_details()

# Child Class

class Bank(User):
    def __init__(self,name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def view_balance(self):
        print(f"Your balance is: ${self.balance}")

person = Bank("Hehe", 24, "Female")

person.deposit(100)
person.view_balance()

person.withdraw(50)
person.view_balance()