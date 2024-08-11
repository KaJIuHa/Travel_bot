from aiogram.fsm.state import State, StatesGroup

class AdminRemove(StatesGroup):
    id_number = State()