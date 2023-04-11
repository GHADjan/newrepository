## в ЗАВИСИМОСТИ ОТ БОТА
 # ИМПОРТИРОВАТЬ НУЖНЫЕ КОМПОНЕНТЫ ИЗ НУЖНОЙ БИБЛИОТЕКИ
# from aiogram import Bot, Dispatcher, executor
#
# from keyboard import
#
#
# ##   1 ###
# bot = Bot('6197130919:AAEfcY3pQtaEgbKdYaY7GVISZZIivFBnvtM')
#
# dp = Dispatcher(bot)
#
#
#
#
# ## 1 ##
# # Запуск всех процессов
# executor.start_polling(dp)
































# ## 2 ###
# #
# # рабочее пространство для обработчика
#
# ## в зависимости от бота ##
# # создаем обработчики
# @dp.message_handler() # текст
# # Ответы на те или иные сообщения
# async def some_f(message):
#     # message.text - это сообщение от пользователя
#
#     if message.text == 'Привет':
#         # ответ на смс
#         await  message.answer('Привет')
#
#     elif message.text == 'Как дела':
#         await message.answer('Хорошо\nКак сам?')
#
#     else:
#         await message.answer('Не понимаю вас')\
#
#
# @dp.message_handler(фильтр)  # локация
# # Ответы на те или иные сообщения
# async def locations(message):
#
#
#     if message.text == 'Привет':
#         # ответ на смс
#         await  message.answer('Привет')
#
#     elif message.text == 'Как дела':
#         await message.answer('Хорошо\nКак сам?')
#
#     else:
#         await message.answer('Не понимаю вас')
#
#
#
#
#
#
#
#
#
#
# @dp.message_handler(commands=['start', 'help'])
# async def start_message(message):
#     answer = 'Привет я самый лучший бот'
#
#     await message.answer(answer, reply_markup=buttons.first_buttons())
#
# # ОБРАБОТЧИК ТЕКСТОВЫХ СООБЩЕНИЙ
#
# @dp.message_handler(content_types=['text'])
# async def text_message(message):
#     if message.text == 'Первая кнопка':
#         await message.answer('Нажал на первую кнопку')
#
#     else:
#         await message.answer(message.text)
#
#
#
#