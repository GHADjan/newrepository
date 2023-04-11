from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage




import buttonsfortgbothomework





# Подключение к боту
bot = Bot("6197130919:AAEfcY3pQtaEgbKdYaY7GVISZZIivFBnvtM")

# Диспечер сообщений
dp = Dispatcher(bot, storage=MemoryStorage())



@dp.message_handler(commands=['start'])
async def start_command(message):
    start_text = f'Привет {message.from_user.first_name}\nЯ бот, который позволит чуть больше узнать обо мне'

    # Получить айди пользователя
    user_id = message.from_user.id
    print(user_id)

    await message.answer(start_text, reply_markup=buttonsfortgbothomework.main_menu())


@dp.message_handler(content_types=['text'])
async def handle_text(message):
    if message.text == 'Расскажи о себе':
        await message.answer('Я начинающий разработчик, меня зовут Жандос и я программирую на языке python🐍',reply_markup=buttonsfortgbothomework.contacts())
    elif message.text == 'Кейсы':
        await message.answer('Выберите Кейс', reply_markup=buttonsfortgbothomework.keys())
    elif message.text == 'Кейс 1':
        await message.answer('Кейс пуст', reply_markup=buttonsfortgbothomework.sledushiy())
    elif message.text == 'Следущий кейс':
        await message.answer('второй кейс тоже пуст', reply_markup=buttonsfortgbothomework.contacts())

    elif message.text == 'Кейс 2':
        await message.answer('второй кейс тоже пуст', reply_markup=buttonsfortgbothomework.contacts())

    elif message.text == 'Контакты':
        await message.answer('Вот контакты @junsizbaby', reply_markup=buttonsfortgbothomework.main_menu())
    else:
        await message.answer('Выберите кнопку', reply_markup=buttonsfortgbothomework.main_menu())



















#Запуск бота
executor.start_polling(dp)






