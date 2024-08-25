from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.orm_requsts import orm

reg = [[InlineKeyboardButton(text='📝 Регистрация', callback_data='registration')]]
reg_kb = InlineKeyboardMarkup(inline_keyboard=reg)


def start_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='🗂️ Каталог туров', callback_data='catalog'),
                InlineKeyboardButton(text='🌎 Визы', callback_data='visa'),
                InlineKeyboardButton(text='🔎 Выбрать тур', callback_data='choise_tur'),
                InlineKeyboardButton(text='🪪 Карта АПЕК', callback_data='apek_card'),
                InlineKeyboardButton(text='🕵️ Стать нашим агентом', callback_data='agent'),
                width=2)

    return builder.as_markup()


no_add = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⛔ Галя у нас ОТМЕНА", callback_data='no_add')]
    ],
    resize_keyboard=True
)

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='↩ Вернутся на главную', callback_data='main')]
],
    resize_keyboard=True
)


async def choise_kb():
    category_list = await orm.get_categories()
    print(category_list)
    builder = InlineKeyboardBuilder()
    for i in category_list:
        builder.row(InlineKeyboardButton(text=f'{i[0]}', callback_data=f'ch_{i[1]}'), width=1)
    builder.row(InlineKeyboardButton(text='↩ Вернутся на главную', callback_data='main'))
    return builder.as_markup()


def catalog_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Владивосток', callback_data='catalog_c_vlad'),
                InlineKeyboardButton(text='Хабаровск', callback_data='catalog_c_habarovsk'),
                InlineKeyboardButton(text='Москва', callback_data='catalog_c_msk'),
                width=2).row(InlineKeyboardButton(text='↩ Вернутся на главную', callback_data='main'), width=1)
    return builder.as_markup()


def visa_catalog():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='🇮🇳 Индия', callback_data='visa_india'),
                InlineKeyboardButton(text='🇨🇳 Китай', callback_data='visa_china'),
                InlineKeyboardButton(text='🇯🇵 Япония', callback_data='visa_japan'),
                InlineKeyboardButton(text='🇹🇭 Тайланд', callback_data='visa_tailand'),
                InlineKeyboardButton(text='🇰🇷 Южная Корея', callback_data='visa_south_korea'),
                InlineKeyboardButton(text='🇸🇬 Сингапур', callback_data='visa_siongopur'),
                InlineKeyboardButton(text='🇹🇼 Тайвань', callback_data='visa_taivan'),
                width=2).row(InlineKeyboardButton(text='↩ Вернутся на главную', callback_data='main'), width=1)
    return builder.as_markup()

async def visa_catalog_price(category):
    category_list = await orm.get_visa_price(category=category)
    print(category_list)
    builder = InlineKeyboardBuilder()
    for i in category_list:
        builder.row(InlineKeyboardButton(text=f'Опалатить: {i[0]}', callback_data=f'pay_{i[1]}_{i[2]}'), width=1)
    builder.row(InlineKeyboardButton(text='↩ Вернутся на главную', callback_data='main'))
    return builder.as_markup()
