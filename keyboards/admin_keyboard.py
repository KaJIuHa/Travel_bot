from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.orm_requsts import orm

no_add = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⛔ Галя у нас ОТМЕНА",
                              callback_data='no_add_admin')]
    ],
    resize_keyboard=True
)

back_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='↩ Вернутся в админ меню',
                              callback_data='admin')]
    ]
)


def admin_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Добавить/изменить в каталог",
                                     callback_data='add_catalog'),
                InlineKeyboardButton(text="Добавить/изменить в визы",
                                     callback_data='add_visa'),
                InlineKeyboardButton(text="Добавить/изменить в Выбор тура",
                                     callback_data='add_choise_tur'),
                InlineKeyboardButton(text="Добавить/изменить кнопку для туров",
                                     callback_data='add_button'),
                InlineKeyboardButton(text="Получить файл с контактами пользователей",
                                     callback_data='get_file'),
                width=1).row(InlineKeyboardButton(text='↩ Вернутся на главную',
                                                  callback_data='main'))
    return builder.as_markup()


def admin_catalog_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Владивосток',
                                     callback_data='acatalog_c_vlad'),
                InlineKeyboardButton(text='Хабаровск',
                                     callback_data='acatalog_c_habarovsk'),
                InlineKeyboardButton(text='Москва',
                                     callback_data='acatalog_c_msk'),
                width=2).row(InlineKeyboardButton(text='↩ Вернутся в админ меню',
                                                  callback_data='admin'),
                             width=1)
    return builder.as_markup()


async def admin_choise_kb():
    category_list = await orm.get_categories()
    builder = InlineKeyboardBuilder()
    for i in category_list:
        builder.row(InlineKeyboardButton(text=f'{i[0]}',
                                         callback_data=f'acatalog_ch_{i[1]}'),
                    width=1)
    builder.row(InlineKeyboardButton(text='↩ Вернутся в админ меню',
                                     callback_data='admin'))
    return builder.as_markup()


def admin_catalog_choise(query):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="📥 Добавить",
                                     callback_data=f'upload_{query}'),
                InlineKeyboardButton(text='🔁Изменить',
                                     callback_data=f'change_{query}'),
                width=2).row(InlineKeyboardButton(text='↩ Вернутся в админ меню',
                                                  callback_data='admin'),
                             width=1)

    return builder.as_markup()


def admin_button_choise():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="📥 Добавить",
                                     callback_data=f'button_upload'),
                InlineKeyboardButton(text='🔁Изменить',
                                     callback_data=f'button_change'),
                InlineKeyboardButton(text='🚫Удалить',
                                     callback_data=f'button_delete'),
                width=2).row(InlineKeyboardButton(text='↩ Вернутся в админ меню',
                                                  callback_data='admin'),
                             width=1)

    return builder.as_markup()


def admin_button_action(action, idx):
    builder = InlineKeyboardBuilder()
    if action == 'change':
        builder.row(InlineKeyboardButton(text='🔁Изменить',
                                         callback_data=f'bchange_{idx}'),
                    width=1)
        return builder.as_markup()
    elif action == 'delete':
        builder.row(InlineKeyboardButton(text='🚫Удалить',
                                         callback_data=f'bdelete_{idx}'),
                    width=1)
        return builder.as_markup()


def admin_change_button(idx):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Изменить',
                                     callback_data=f'idx_{idx}'),
                width=1)
    return builder.as_markup()


def super_admin_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Посмотреть ID администраторов',
                                     callback_data='show_admins'),
                InlineKeyboardButton(text='Добавить администратора',
                                     callback_data='add_admin'),
                InlineKeyboardButton(text='Удалить администртора',
                                     callback_data='remove_admin'),
                width=1)
    return builder.as_markup()


def button_choise_kb(button_idx):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="⬆Изменить⬆",
                                     callback_data=f'changebutton_{button_idx}'))
    return builder.as_markup()


def button_delete_kb(button_idx):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="⬆🚫Удалить⬆",
                                     callback_data=f'deletebutton_{button_idx}'))
    return builder.as_markup()


def admin_visa_choise():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="📥 Добавить",
                                     callback_data=f'avisa_upload'),
                InlineKeyboardButton(text='🔁Изменить',
                                     callback_data=f'avisa_change'),
                width=2).row(InlineKeyboardButton(text='↩ Вернутся в админ меню',
                                                  callback_data='admin'),
                             width=1)

    return builder.as_markup()


def upload_visa_catalog():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='🇮🇳 Индия',
                                     callback_data='uvisa_india'),
                InlineKeyboardButton(text='🇨🇳 Китай',
                                     callback_data='uvisa_china'),
                InlineKeyboardButton(text='🇯🇵 Япония',
                                     callback_data='uvisa_japan'),
                InlineKeyboardButton(text='🇹🇭 Тайланд',
                                     callback_data='uvisa_tailand'),
                InlineKeyboardButton(text='🇰🇷 Южная Корея',
                                     callback_data='uvisa_south_korea'),
                InlineKeyboardButton(text='🇸🇬 Сингапур',
                                     callback_data='uvisa_siongopur'),
                InlineKeyboardButton(text='🇹🇼 Тайвань',
                                     callback_data='uvisa_taivan'),
                width=2).row(InlineKeyboardButton(text="⛔ Галя у нас ОТМЕНА",
                                                  callback_data='no_add_admin'),
                             width=1)
    return builder.as_markup()
