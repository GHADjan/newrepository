# def fuct(a, b):
#     return a+b
# print(fuct(5,5))
#
#
# def slova(spam):
#      for i in spam:
#          if 'a' in i:
#              print(i)
#
# slova(['anna', 'mike'])
#
#
#
#
#
# def plov(spam):
#     return max(spam)
# print(plov([3,3123,123,413,123,64,645]))




class Book:
    def __init__(self, name, avtor, izdatelstvo, date):
        self.name = name
        self.avtor = avtor
        self.izdatelstvo = izdatelstvo
        self.date = date


    def show(self):
        return f'{self.name}, {self.avtor},{self.izdatelstvo},{self.date}'



book = Book(name='гарри потерр', avtor='neznayu', izdatelstvo='toje ne znayu', date='fig znaet kogda')

print(book.show())




class Human:
    def __init__(self, name, surname, age, sex,):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex

    def show(self):
        return f'{self.name}, {self.surname},  {self.age},  {self.sex}, на следущий год ему-'


    def happy_birthday(self, a=1):
        self.age = self.age + a
        return self.age





human = Human(name='pasha', surname='pavlov', age=23,  sex='мужской',)
print(human.show())
print(human.show(), human.happy_birthday())
print(human.show(), human.happy_birthday())
print(human.show(), human.happy_birthday())
print(human.show(), human.happy_birthday())
print(human.show(), human.happy_birthday())

