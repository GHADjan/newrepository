from aiogram.dispatcher.filters.state import State, StatesGroup






# Процесс сбора информации
## Процесс - это класс, а Этапы - это переменные
class GetData(StatesGroup):
    get_name_state = State()
    get_number_state = State()
    get_location_state = State()
    get_resume_state = State()


















