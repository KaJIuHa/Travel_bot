from aiogram.filters import BaseFilter
from aiogram import types


class Admin(BaseFilter):
    """Класс проверки администраторов"""

    async def __call__(self, msg: types.Message):
        return msg.from_user.id in [5630610750,1891942484]