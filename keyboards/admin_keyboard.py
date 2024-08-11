from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

no_add = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⛔ Галя у нас ОТМЕНА", callback_data='no_add_admin')]
    ],
    resize_keyboard=True
)

back_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='↩ Вернутся в админ меню', callback_data='admin')]
    ]
)


def admin_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Добавить/изменить в каталог", callback_data='add_catalog'),
                InlineKeyboardButton(text="Добавить/изменить в визы", callback_data='acatalog_visa'),
                InlineKeyboardButton(text="Добавить/изменить в Выбор тура", callback_data='add_choise_tur'),
                InlineKeyboardButton(text="Получить файл с контактами пользователей", callback_data='get_file'),
                width=1).row(InlineKeyboardButton(text='↩ Вернутся на главную', callback_data='main'))
    return builder.as_markup()


def admin_catalog_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Владивосток', callback_data='acatalog_c_vlad'),
                InlineKeyboardButton(text='Хабаровск', callback_data='acatalog_c_habarovsk'),
                InlineKeyboardButton(text='Москва', callback_data='acatalog_c_msk'),
                width=2).row(InlineKeyboardButton(text='↩ Вернутся в админ меню', callback_data='admin'), width=1)
    return builder.as_markup()


def admin_choise_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='🇷🇺 Владивосток', callback_data='acatalog_сh_vlad'),
                InlineKeyboardButton(text='🇷🇺 Санкт-Петербург', callback_data='acatalog_ch_spb'),
                InlineKeyboardButton(text='🇷🇺 Москва', callback_data='acatalog_ch_msk'),
                InlineKeyboardButton(text='🇨🇳 Китай', callback_data='acatalog_ch_china'),
                InlineKeyboardButton(text='🚀 Вочточный', callback_data='ch_vostochniy'),
                InlineKeyboardButton(text='🛸 Байконур', callback_data='ch_boukonyr'),
                InlineKeyboardButton(text='🇷🇺 Сахалин', callback_data='acatalog_ch_saha'),
                InlineKeyboardButton(text='🇷🇺 Казань', callback_data='acatalog_ch_kazan'),
                InlineKeyboardButton(text='🇷🇺 Дагестан', callback_data='acatalog_ch_dag'),
                InlineKeyboardButton(text='🇧🇾 Белоруссия', callback_data='acatalog_ch_bel'),
                width=1).add(InlineKeyboardButton(text='↩ Вернутся в админ меню', callback_data='admin'))
    return builder.as_markup()


def admin_catalog_choise(query):
    print(query)
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="📥 Добавить", callback_data=f'upload_{query}'),
                InlineKeyboardButton(text='🔁Изменить', callback_data=f'change_{query}'),
                width=2).row(InlineKeyboardButton(text='↩ Вернутся в админ меню', callback_data='admin'), width=1)

    return builder.as_markup()


def admin_change_button(idx):
    print(idx)
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Изменить',
                                     callback_data=f'idx_{idx}'),
                width=1)
    return builder.as_markup()

def super_admin_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Посмотреть ID администраторов',callback_data='show_admins'),
                InlineKeyboardButton(text='Добавить администратора',callback_data='add_admin'),
                InlineKeyboardButton(text='Удалить администртора',callback_data='remove_admin'),width=1)
    return builder.as_markup()