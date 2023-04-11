from aiogram.dispatcher.filters.state import State, StatesGroup

# Процессы для регистрации
class Registration(StatesGroup):
    getting_name_state = State()
    getting_phone_number = State()
    getting_location = State()
    getting_gender = State()



# Процессы для выбора определенного товара
class GetProduct(StatesGroup):
    getting_pr_name = State()
    getting_pr_count = State()





# Процессы при работе с корзиной
class Cart(StatesGroup):
    waiting_for_product = State()
    waiting_new_product = State()





# Процессы при оформлений заказа
class Order(StatesGroup):
    waiting_location = State()
    waiting_pay_type = State()
    waiting_accept = State()






