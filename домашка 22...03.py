#
#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def greeting(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет.")


person = Person("Иван", 25)
person.greeting()
#
#
#
#
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

rectangle = Rectangle(5, 10)
area = rectangle.get_area()
print(f"Площадь прямоугольника: {area}")
#
#
#
#
#
#
#
class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.positon = position
        self.salary = salary


    def display_info(self):
        print(f"Информация о сотруднике:{self.name}, {self.age}, {self.positon}, {self.salary}")

person = Employee(name='Pasha', age='23', position='neznayu', salary='toje neznayu')
person.display_info()

#
#
#
#
#
#
#
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount


account = BankAccount("pashsa", 1000)
print("Starting balance:", account.balance)
account.deposit(500)
print("New balance after deposit:", account.balance)
account.withdraw(200)
print("New balance after withdrawal:", account.balance)
account.withdraw(2000)

#
#
#
#
#
#
#
class User:
    def __init__(self, name, email, age, phone):
        self.name = name
        self.email = email
        self.age = age
        self.phone = phone

    def change_username(self, new_name):
        self.name = new_name

    def change_number(self, new_number):
        self.phone = new_number

    def change_mail(self, new_mail):
        self.email = new_mail


# Создаем экземпляр класса
user = User("John", "john@example.com", 30, "123-456-7890")

# Выводим начальные данные
print("name:", user.name)
print("email:", user.email)
print("age:", user.age)
print("phone number:", user.phone)

# Изменяем имя
user.change_username("Peter")

# Изменяем номер телефона
user.change_number("987-654-3210")

# Изменяем почту
user.change_mail("peter@example.com")

# Выводим измененные данные
print("New name:", user.name)
print("New email:", user.email)
print("New age:", user.age)
print("New phone number:", user.phone)