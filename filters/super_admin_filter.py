from aiogram.filters import BaseFilter
from aiogram import types


class SuperAdmin(BaseFilter):
    """Класс проверки суперадмина"""
    async def __call__(self, msg: types.Message):
        return msg.from_user.id in [5630610750,1891942484]