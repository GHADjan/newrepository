
#.append()
#.remove()
#spisok(index) = new_name



users = []

admin = input('что вы хотмте сделать: ')


# проверка
if admin == 'добавить':
    # запращиваем новый номер
    new_number = input('введите номер: ')


    # добавить в список
    users.append(new_number)


# еслм пользоывтель хочет удалить
elif admin == 'удалить':
    number = input('кого удалить: ')

    # удаление введенного номера из саиска
    users.remove(number)