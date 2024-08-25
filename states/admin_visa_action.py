from aiogram.fsm.state import State, StatesGroup

class AdminUploadVisa(StatesGroup):
    visa_category = State()
    visa_photo_id = State()