from oauth2client.service_account import ServiceAccountCredentials
import gspread

# Список Ссылок где нужно пройти авторизацию
scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

# Подключение необходимых ключей
creds = ServiceAccountCredentials.from_json_keyfile_name('credents.json', scope)

# На какой именно сервис нужно авторизоваться
client = gspread.authorize(creds)


# открываем нужную таблицу
tablica1 = client.open('pythonfull')


# Открыть нужный лист

list1 = tablica1.worksheet('Лист1')


while True:
    admin = input('что вы хотите сделать: ')
    if admin == 'добавить клиента':

        client_name = input('Введите имя: ')
        client_age = int(input('Введите возраст: '))
        client_room = input('Введите комнаты: ')

        # Добавить полученные данные в таблицу
        list1.append_row([client_name, client_age, client_room])


    elif admin == 'удалить клиента':
        room_number = input('из какой комнаты удаляем: ')
        # Нужно найти строку с этой комнатой в листе
        room = list1.find(room_number)
        list1.delete_rows(room.row)
    elif admin == 'изменить номер':
        room_number2 = input('какую комнату меняем: ')
        new_room_number = input('на какой номер меняем: ')

        room2 = list1.find(room_number2)
        list1.update_cell(room2.row, 3, new_room_number)





        # Получить все данные из листа
        all_data = list1.get_all_records()
        print(all_data)
