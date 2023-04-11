from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove

import buttons2

from states import GetData




# Подключение к боту
bot = Bot("6085895003:AAE2IZ92KI4ZCcQJ6WPiDkJbuO60KoJXeeU")

# Диспечер сообщений
dp = Dispatcher(bot, storage=MemoryStorage())

# Обработчик команды start
@dp.message_handler(commands=['start'])
async def start_command(message):
    start_text = f'Привет {message.from_user.first_name}\nЯ автоматизированный HR отдел компании AiogramBot'

    # Получить айди пользователя
    user_id = message.from_user.id
    print(user_id)


    # Ответ
    await message.answer(start_text, reply_markup=buttons2.main_menu())

# Обработчик текстовых сообщений (всех основных кнопок)
@dp.message_handler(content_types=['text'])
async def text_messsage(message):
    # Прописываем условия для кнопки главного меню
    if message.text == 'Отправить резюме':

        await message.answer('Отлично\nСперва отправь имя', reply_markup=ReplyKeyboardRemove())

        # Переход на этап получения имени
        await GetData.get_name_state.set()


    elif message.text == 'Статус':
        resume_id = 'BQACAgIAAxkBAANaZDGBESYT6w4a8uP8XKKqMYTlPCwAAvoqAAIIc4lJcjeoQ3TDt18vBA'

        # Отправляем документ
        await message.answer_document(resume_id)
        await message.answer('Ваше резюме еще не просмотрено')



    else:
        await message.answer('Выберите кнопку', reply_markup=buttons2.main_menu())


# Обработчик этапа получения имени
@dp.message_handler(state=GetData.get_name_state)
async def get_name(message, state=GetData.get_name_state):
    name = message.text
    # Сохраняем во временную базу имя пользователя
    await state.update_data(user_name=name)


    await message.answer('Отправь теперь свой номер телефона', reply_markup=buttons2.phone_number_kb())

    # Переход на этап получения номера телефона
    await GetData.get_number_state.set()


# Обработчик этапа получения номера
@dp.message_handler(state=GetData.get_number_state, content_types=['contact'])
async def get_phone_number(message, state=GetData.get_number_state):
    # Сохраняем локально номер телефона
    user_number = message.contact.phone_number
    await state.update_data(phone_number=user_number)

    # Сохраняем в переменную номер телефона
    user_number = message.contact.phone_number

    await message.answer('Отправь теперь свою локацию', reply_markup=buttons2.location_kb())

    # Переход на этап получения локации

    await GetData.get_location_state.set()

# Обработчик этапа получения локации
@dp.message_handler(state=GetData.get_location_state, content_types=['location'])
async def get_location(message, state=GetData.get_location_state):
    user_location = message.location.latitude, message.location.longitude
    # Сохраняем локацию
    await state.update_data(coordinates=user_location)


    lat = message.location.latitude
    lon = message.location.longitude
    # Отправить ответ об успешном получений
    await message.answer('Локация принята\nОтправьте файл с резюме', reply_markup=ReplyKeyboardRemove())

    await GetData.get_resume_state.set()



@dp.message_handler(state=GetData.get_resume_state, content_types=['document'])
async def get_resume(message, state=GetData.get_resume_state):
    # Сохраняем уникальный айди документа
    user_cv = message.document.file_id


    # Выгружаем всю информацию полученную от пользователя
    all_info = await state.get_data()

    admin_message  = f'Новые резюме 🌚\nИмя: {all_info["user_name"]}\nНомер телефона: {all_info["phone_number"]}\nЛокация и Резюме:'

    await bot.send_message(1088568707, admin_message)

    await bot.send_location(1088568707, latitude=all_info["coordinates"][0], longitude=all_info["coordinates"][1])

    await bot.send_document(1088568707, document=user_cv)

    await message.answer('Ваши данные сохранены и переданы в базу', reply_markup=buttons2.main_menu())

    await state.finish()














#Запуск бота
executor.start_polling(dp)



###########        BQACAgIAAxkBAANaZDGBESYT6w4a8uP8XKKqMYTlPCwAAvoqAAIIc4lJcjeoQ3TDt18vBA