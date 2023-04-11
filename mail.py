mail = input('введите почтe: ')
password = input('введите пароль: ')
password2 = input('введите пароль повторно: ')

# проверка почты
if '@' in mail and password == password2:
    print('это почта')
    print('успешный вход')

elif password != password2:
    print('пароли не совпадают')

else:
    print('это не почта')