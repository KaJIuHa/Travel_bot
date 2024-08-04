from aiogram.fsm.state import State, StatesGroup

class UserRegister(StatesGroup):
    name = State()
    phone = State()
    email = State()
