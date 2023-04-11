from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



# ОСнвная кнопка
def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True,)
    send = KeyboardButton('Расскажи о себе')
    keys = KeyboardButton('Кейсы')
    kb.add(send, keys)

    return kb


def contacts():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    contacts = KeyboardButton('Контакты')
    back = KeyboardButton('Назад')
    kb.add(contacts, back)
    return kb

def keys():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    keys1 = KeyboardButton('Кейс 1')
    # sled = KeyboardButton('Следущий кейсы')
    keys2 = KeyboardButton('Кейс 2')
    kb.add(keys1, keys2)
    return kb


def sledushiy():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    sledushiy = KeyboardButton('Следущий кейс')

    kb.add(sledushiy)
    return kb
