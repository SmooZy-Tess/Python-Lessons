print("-----------Number 1-----------")

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
        else:
            print('Нельзя внести отрицательную сумму!!!')
    
    def withdraw(self, amount):
        if amount >= 0:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print('Недостаточно денег для снятия!')
        else:
            print('Нельзя снять отрицательную сумму денег!!!')
    
    def get_balance(self):
        return self.__balance
    
    def create_empty_account(cls, account_number):
        return cls(account_number, 0)

acc = BankAccount.create_empty_account(BankAccount, '123456789')
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())

print("-----------Number 2-----------")

class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    
    def hard_password(self, password):
        return len(password) <= 5

    def create_defolt_user(cls, username):
        dpass = "DefoltPass"
        return cls(username, dpass)

    def set_password(self, new_password):
        if self.hard_password(new_password):
            print("Пароль слишком легкий, нужно больше 6 символов!!!")
        else:
            self.__password = new_password
            print("Пароль был успешно изменен!")

    def get_username(self):
        return self.__username

user = User.create_defolt_user(User, "Alice")
print(user.get_username())

user.set_password("12345")
user.set_password("securePass")

print("-----------Number 3-----------")

class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = self.check_year(year)

    def check_year(self, year):
        if year >= 0 and year <= 2025:
            return year
        else:
            print("Год указан неправильно!!!")

    def create_default_year(cls, title, author):
        default_year = 2024
        return cls(title, author, default_year)

    def get_info(self):
        return f"{self.__title}, автор: {self.__author}, год: {self.__year}"

book1 = Book("1984", "George Orwell", 1949)
print(book1.get_info())

book2 = Book.create_default_year(Book, "Brawe New World", "Aidous Huxley")
print(book2.get_info())