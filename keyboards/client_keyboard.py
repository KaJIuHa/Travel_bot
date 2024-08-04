from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

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


def choise_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='🇷🇺 Владивосток', callback_data='сh_vlad'),
                InlineKeyboardButton(text='🇷🇺 Санкт-Петербург', callback_data='ch_spb'),
                InlineKeyboardButton(text='🇷🇺 Москва', callback_data='ch_msk'),
                InlineKeyboardButton(text='🇨🇳 Китай', callback_data='ch_china'),
                InlineKeyboardButton(text='🚀 Космодром', callback_data='kosmodrom'),
                InlineKeyboardButton(text='🇷🇺 Сахалин', callback_data='ch_saha'),
                InlineKeyboardButton(text='🇷🇺 Казань', callback_data='ch_kazan'),
                InlineKeyboardButton(text='🇷🇺 Дагестан', callback_data='ch_dag'),
                InlineKeyboardButton(text='🇧🇾 Белоруссия', callback_data='ch_bel'),
                width=1).add(InlineKeyboardButton(text='↩ Вернутся на главную', callback_data='main'))
    return builder.as_markup()


def choise_kosmo():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='🚀 Вочточный', callback_data='ch_vostochniy'),
                InlineKeyboardButton(text='🛸 Байконур', callback_data='ch_boukonyr'),
                width=2).row(InlineKeyboardButton(text='↩ Вернуться в предидущее меню',
                                                  callback_data='choise_tur'),
                             width=1
                             ).row(InlineKeyboardButton(text='↩ Вернутся на главную',
                                                        callback_data='main'),
                                   width=1)
    return builder.as_markup()


def catalog_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Владивосток', callback_data='catalog_c_vlad'),
                InlineKeyboardButton(text='Хабаровск', callback_data='catalog_c_habarovsk'),
                InlineKeyboardButton(text='Москва', callback_data='catalog_c_msk'),
                width=2).row(InlineKeyboardButton(text='↩ Вернутся на главную', callback_data='main'), width=1)
    return builder.as_markup()
