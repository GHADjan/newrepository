username = input('введите имя: ')
password = input('введите пароль: ')
password2 = input('введите пароль повторно: ')

# Проверка паролей
if password == password2:
    print('успешный вход')

else:
    print('пароли отличаются')
