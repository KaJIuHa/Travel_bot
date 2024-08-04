from aiogram.fsm.state import State, StatesGroup

class AdminUpload(StatesGroup):
    photo = State()