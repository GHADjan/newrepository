
def say_helllo():
    print('Hello world')
#Вызов функции
say_helllo()




def creat_list():
    my_list = []
    print(my_list)
    # Вызов функции
creat_list()


def calc():
    print(3+5)
calc()



def proffesia():
    print('Я уже программист')
proffesia()



def spam():
    print('spammer')




def list_generator():
    user = ['jordan']
    return user

u = list_generator()

u.append('pasha')

print(u)

# пропуск функции
def my1():
    pass



def creat_instructor():
    instructor = {'name':'jordan', 'age': 21, 'job': 'programmer'}

    if 'name' in instructor:
        return 'Да есть'

    else:
        return 'Не понимаю о чем вы'

creat_instructor()



# проверка
def check_user(mail):
    users = ['sasha@mail','pasha@mail', 'jordan@mail']
    if mail in users:
        return 'такой уже есть'

    #процесс регистрации
    return 'успешно зарегистрирован'
#blabla = input('Введите почту: ')
r = check_user('blabla')
m = check_user(mail='blabla')
#print(m)


# функция подставления
def spam2(a):
    print(a+6)
spam2(3)




def summa(a, b):
    return a+b

print(summa(5,5))

