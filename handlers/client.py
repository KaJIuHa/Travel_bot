import asyncio
import datetime

from aiogram import types, F, Router
from aiogram.enums import ChatAction
from aiogram.filters import CommandStart,Command
from aiogram.fsm.context import FSMContext
import phonenumbers
from email_validator import validate_email

import keyboards.client_keyboard as kb
from utils.texts import Texts

from create_bot import bot
from database.orm_requsts import orm
from states.register import UserRegister

cl_route = Router()


@cl_route.message(CommandStart())
async def cmd_start(msg: types.Message):
    """Команда старт и проверка пользователя на наличие в БД"""
    if await orm.check_user(msg.from_user.id):
        await msg.answer(text=Texts.START,
                         reply_markup=kb.start_kb())
    else:
        await msg.answer(text=Texts.start(msg.from_user.username),
                         reply_markup=kb.reg_kb)

@cl_route.message(Command('about_us'))
async def about_us_handler(msg:types.Message):
    content = types.FSInputFile('data/about_us.jpg')
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=content,
                         caption=Texts.ABOUT_US,
                         protect_content=True)
@cl_route.message(Command('my_id'))
async def my_id_handler(msg:types.Message):
    await bot.send_message(msg.from_user.id,
                           text=Texts.my_id(int(msg.from_user.id)))

@cl_route.callback_query(F.data == 'main')
async def main(call: types.CallbackQuery):
    """Главное меню"""
    if await orm.check_user(call.from_user.id):
        await call.message.edit_text(text=Texts.START,
                                     reply_markup=kb.start_kb())
    else:
        await call.message.edit_text(text=Texts.start(call.from_user.username),
                                     reply_markup=kb.reg_kb)


@cl_route.callback_query(F.data == 'registration')
async def start_client_registery(call: types.CallbackQuery, state: FSMContext):
    """Хендлер начала регистрации"""
    await call.message.edit_text(text=Texts.ADD_NAME,
                                 reply_markup=kb.no_add)
    await state.update_data(id=call.from_user.id,
                            username=call.from_user.username)
    await state.set_state(UserRegister.name)
    await call.answer(cache_time=2)


@cl_route.message(UserRegister.name)
async def add_name_registery(msg: types.Message, state: FSMContext):
    """Хендлер добавления имени"""
    if msg.text.isalpha():
        await state.update_data(name=msg.text)
        await state.set_state(UserRegister.phone)
        await bot.send_message(msg.from_user.id,
                               text=Texts.ADD_PHONE,
                               reply_markup=kb.no_add)
    else:
        await bot.send_message(msg.from_user.id,
                               text=Texts.ER_ADD_NAME,
                               reply_markup=kb.no_add
                               )
        await state.set_state(UserRegister.name)


@cl_route.message(UserRegister.phone)
async def add_phone_registery(msg: types.Message, state: FSMContext):
    """Хендлер добавления номера телефона"""
    phone_number = phonenumbers.parse(msg.text)
    valid = phonenumbers.is_valid_number(phone_number)
    if valid:
        await state.update_data(phone=msg.text)
        await state.set_state(UserRegister.email)
        await bot.send_message(msg.from_user.id,
                               text=Texts.ADD_EMAIL,
                               reply_markup=kb.no_add)
    else:
        await bot.send_message(msg.from_user.id,
                               text=Texts.ER_ADD_PHONE,
                               reply_markup=kb.no_add)
        await state.set_state(UserRegister.phone)


@cl_route.message(UserRegister.email)
async def add_email_registery(msg: types.Message, state: FSMContext):
    """Хендлер добавления емайл и записи в БД"""
    try:
        validate_email(msg.text)
        await state.update_data(email=msg.text)
        data = await state.get_data()
        try:
            await orm.create_user(data)
            await state.clear()
            await bot.send_message(msg.from_user.id,
                                   text=Texts.SUCC_ADD,
                                   reply_markup=kb.main)
        except Exception as er:
            print(er)
            await state.clear()
            await bot.send_message(msg.from_user.id,
                                   text=Texts.ER_ADD_COMPLITE,
                                   reply_markup=kb.main)
    except Exception as ex:
        print(ex)
        await state.set_state(UserRegister.email)
        await bot.send_message(msg.from_user.id,
                               text=Texts.ER_ADD_EMAIL,
                               reply_markup=kb.no_add)


@cl_route.callback_query(F.data == 'no_add')
async def no_add_call(call: types.CallbackQuery, state: FSMContext):
    """Хендлер отмены"""
    await state.clear()
    await call.answer(text='Галя,отменила 👌')


@cl_route.callback_query(F.data == 'apek_card')
async def apek_handler(call: types.CallbackQuery):
    await call.message.edit_text(text=Texts.APEK,
                                 reply_markup=kb.main)
    await call.answer(cache_time=2)


@cl_route.callback_query(F.data == 'agent')
async def agent_handler(call: types.CallbackQuery):
    await call.message.edit_text(text=Texts.AGENT,
                                 reply_markup=kb.main)
    await call.answer(cache_time=2)


@cl_route.callback_query(F.data == 'catalog')
async def catalog_handler(call: types.CallbackQuery):
    await call.message.edit_text(text=Texts.CATALOG,
                                 reply_markup=kb.catalog_kb())


@cl_route.callback_query(F.data.startswith('catalog_'))
async def send_catalog(call: types.CallbackQuery):
    photos = await orm.get_files(category=call.data[8::])
    action = ChatAction.UPLOAD_PHOTO

    group = []
    for photo in photos:
        group.append(types.InputMediaPhoto(media=photo, caption=Texts.CAPTION))
    await bot.send_chat_action(call.from_user.id, action=action)
    await asyncio.sleep(3)
    await call.message.answer_media_group(media=group, protect_content=True)
    await bot.send_message(call.from_user.id, text=Texts.CAPTION, reply_markup=kb.catalog_kb())


@cl_route.callback_query(F.data == 'choise_tur')
async def choise_tur(call: types.CallbackQuery):
    await call.message.edit_text(text=Texts.CHOISE_TUR,
                                 reply_markup=await kb.choise_kb())


@cl_route.callback_query(F.data.startswith('ch_'))
async def send_catalog(call: types.CallbackQuery):
    photos = await orm.get_files(category=call.data)
    action = ChatAction.UPLOAD_PHOTO
    group = []
    for photo in photos:
        group.append(types.InputMediaPhoto(media=photo, caption=Texts.CAPTION))
    await bot.send_chat_action(call.from_user.id, action=action)
    await asyncio.sleep(3)
    await call.message.answer_media_group(media=group, protect_content=True)
    await bot.send_message(call.from_user.id, text=Texts.CAPTION, reply_markup=kb.choise_kb())


@cl_route.callback_query(F.data == 'kosmodrom')
async def kosmodrom_handler(call: types.CallbackQuery):
    await call.message.edit_text(text=Texts.CHOISE_KOSMO,
                                 reply_markup=kb.choise_kosmo())
    await call.answer(cache_time=2)


@cl_route.callback_query(F.data == 'visa')
async def visa_hendler(call: types.CallbackQuery):
    photos = await orm.get_files(category=call.data)
    action = ChatAction.UPLOAD_PHOTO
    group = []
    for photo in photos:
        group.append(types.InputMediaPhoto(media=photo, caption=Texts.CAPTION))
    await bot.send_chat_action(call.from_user.id, action=action)
    await asyncio.sleep(3)
    await call.message.answer_media_group(media=group, protect_content=True)
