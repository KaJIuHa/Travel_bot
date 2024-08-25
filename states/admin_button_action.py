from aiogram.fsm.state import State, StatesGroup


class AdminButtonActionUpload(StatesGroup):
    button_name = State()


class AdminButtonActionDelete(StatesGroup):
    button_idx = State()


class AdminButtonActionChange(StatesGroup):
    button_idx = State()
    button_name = State()
