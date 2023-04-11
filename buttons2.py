from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# ОСновные кнопки
def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    send = KeyboardButton('Отправить резюме')
    status = KeyboardButton('Статус')

    kb.add(send, status)

    return kb




# Кнопки для получения номера телефона

def phone_number_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    number = KeyboardButton('Поделиться контактом', request_contact=True)

    kb.add(number)
    return kb


#Кнопка для получения локации
def location_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    location = KeyboardButton('Отправить локацию', request_location=True)

    kb.add(location)

    return kb


