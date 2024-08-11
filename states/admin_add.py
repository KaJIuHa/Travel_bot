from aiogram.fsm.state import State, StatesGroup

class AdminAdd(StatesGroup):
    id_number = State()