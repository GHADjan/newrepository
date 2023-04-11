# Создать переменную со значением integer
chisla = int(12)
# Создать переменную со значением string
slova = str('pasha')
# Создать переменную со значением float
chisla1 = float(1.1)
# Создать лист, который содержит в себе (int, str, tuple, list, dict)

list = ['chisla' , 12 , 2.0, (1,2,3), [4,5,6], {'name':'pasha'}]
print(list)
print(type(list))



# Привести пример на list comprehension, который отбирает все слова, которые содержат букву d
n = ['drum', 'danger', 'card', 'pasha', 'yard', 'crud', 'drug'] 
m = [i for i in n if 'd' in i]
print(m)
# Создать примерный стэк юзера используя словарь
m = {'id': '0', 'login': 'blabla', 'parol':'123'}
print(m)
# Создать словарь, значение которого является другим словарем
a = {}
# Используя цикл пройтись по списку и найти все имена с буквой 'd'
p = ['drum', 'danger', 'card', 'pasha', 'yard', 'crud', 'drug'] 
q = [i for i in p if 'd' in i]
print(q)






### Homework ###
# Написать filter() функцию, которая проверяет есть ли цифра 5 в списке
def filters(m):
    for i in m:
        if '5' in str(i):
            return True
    return False

m = [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]
print(filters(m))





# Отсортировать список, сделать его без повторяющихся элементов
n = [1,2,3,3,4,5,5,5,6,7,8,9,9, 'Jordan', 'Pavel', 
'Pasha', 'Kim', 'Drag', 'Messi', 'Ronaldo', 
'Neymar', 'Jordan', 'Pavel', 'Pasha', 2,3,3,4,
'Kim', 'Drag','Drag', 'Messi', 'Ronaldo', 
'Neymar', 'Jordan', 'Pavel', 'Pasha']

print(set(n))

# Создать функцию которая проверяет есть ли некий элемент внутри списка
def func():
    for i in m:
        if '' in i:
            return True
    return False

# Написать функцию с параметром, которая переворачивает текст
def Zadom(potolok):
    return potolok[::-1]
potolok = 'nastok'
pol = Zadom(potolok)
print(pol)
## Задача 1 ##

##Напишите программу с классом Math.
class Math:
    def __init__(self, a ,b):
    #Создайте два атрибута — a и b.
        self.a = a
        self.b = b
#Напишите методы addition — сложение, subtraction — вычитание.
    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b
#При передаче в методы параметров a и b с ними нужно производить
#соответствующие действия и печатать ответ.
k = Math(5,2)
print(k.addition())
print(k.subtraction())

## Задача 2 ##

## Напишите программу с классом Car.
#Создайте конструктор класса Car.
#Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
#Напишите пять методов. 
#Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен». 
#Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». 
class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    def start(self):
        return 'Автомобиль заведен'

    def off(self):
        return 'Автомобиль заглушен'
    def left(self):
        return 'Повернул налево'
    def right(self):
        return 'Повернул направо'
    def info(self):
        return f'{self.color} {self.type} {self.year} '


matiz = Car(color='Красный', type='Седан', year='2009 года')
print(matiz.info(),matiz.start())
print(matiz.info(),matiz.off())
print(matiz.info(),matiz.right())
print(matiz.info(),matiz.left())
print(matiz.info(),matiz.off())
## Пример на наследование
# Создать родительский класс NoutBook (обьеденить все что присуще к ноутам)
# Под него создать подклассы HP, MacBook, Lenovo с отличительными свойствами и методами
#
class Noutbook:
    def __init__(self, model, screen_size, price):
        self.model = model
        self.screen_size = screen_size
        self.price = price
    def turn_on(self):
        return f'{self.model} Включен'
    def turn_off(self):
        return f'{self.model} Выключен'

class HP(Noutbook):
    def __init__(self, model, screen_size, price, battery_life):
        super().__init__(model, screen_size, price)
        self.battery_life = battery_life
    def checkbatter(self):
        return f'У {self.model} {self.battery_life} заряда'

class MacBook(Noutbook):
    def __init__(self,model, screen_size, price, color):
        super().__init__(model, screen_size, price)
        self.color = color

    def change_color(self, new_color):
        self.color = new_color
        return f'{self.model} поменял цвет c {self.color} на {new_color}'

class Lenovo(Noutbook):
    def __init__(self, model, screen_size, price, touch_screen):
        super().__init__(model, screen_size,price)
        self.touch_screen = touch_screen
    def usetouch(self):
        if self.touch_screen:
            return print(f'используется тач скрин на {self.model}')
        else:
            return print(f'{self.model} не имеет тач скрин')

