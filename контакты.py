contacts = []

while True:
    admin = input('Что хотите сделать? ')
    if admin.lower() == 'добавить':
        new_contact = input('Кого добавить? ')
        if new_contact in contacts:
            print('Этот контакт уже есть! Попробуйте другой!')
        else:
            contacts.append(new_contact)
            print('Контакт успешно добавлен!')
    elif admin.lower() == 'изменить':
        contact_to_change = input('Кого изменить? ')
        if contact_to_change in contacts:
            change = input('На кого? ')
            index_cont = contacts.index(contact_to_change)
            contacts[index_cont] = change
            print('Контакт изменен!')
        else:
            print('Такого контакта нет!')
    elif admin.lower() == 'удалить':
        contact_to_remove = input('Кого удалить? ')
        if contact_to_remove in contacts:
            contacts.remove(contact_to_remove)
            print('Контакт удален!')
        else:
            print('Такого контакта нет!')
    elif admin.lower() == 'список':
        print(contacts)
    else:
        print('Нипонял')