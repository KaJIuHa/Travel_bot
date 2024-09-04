import os
import pandas as pd
import datetime
from aiogram import types, F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from create_bot import bot
import keyboards.admin_keyboard as kb
from utils.texts import Texts
from filters.admin_filter import Admin, Admin_list
from filters.super_admin_filter import SuperAdmin
from states.upload import AdminUpload
from states.change import AdminChange
from states.admin_add import AdminAdd
from states.admin_remove import AdminRemove
from states.admin_button_action import (AdminButtonActionUpload,
                                        AdminButtonActionDelete,
                                        AdminButtonActionChange)
from states.admin_visa_action import AdminUploadVisa
from database.orm_requsts import orm

ad_route = Router()


@ad_route.message(Command('admin'), Admin())
async def cmd_admin(msg: types.Message):
    await bot.send_message(msg.from_user.id,
                           text=Texts.ADMIN_START,
                           reply_markup=kb.admin_kb())


@ad_route.callback_query(F.data == 'admin', Admin())
async def admin_menu(call: types.CallbackQuery):
    await call.message.edit_text(text=Texts.ADMIN_START,
                                 reply_markup=kb.admin_kb())
    await call.answer(cache_time=2)


@ad_route.callback_query(F.data == 'add_catalog', Admin())
async def add_catalog_handler(call: types.CallbackQuery):
    await call.message.edit_text(text=Texts.ADMIN_CATALOG,
                                 reply_markup=kb.admin_catalog_kb())
    await call.answer(cache_time=2)


@ad_route.callback_query(F.data.startswith('acatalog_'), Admin())
async def add_catalog_start(call: types.CallbackQuery):
    await call.message.edit_text(
        text=Texts.ADMIN_CATALOG_CHOISE,
        reply_markup=kb.admin_catalog_choise(query=call.data[9::])
    )
    await call.answer(cache_time=2)


@ad_route.callback_query(F.data.startswith('upload_'), Admin())
async def upload_files_admin(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(text=Texts.ADMIN_ADD,
                                 reply_markup=kb.no_add)
    await state.update_data(category=call.data[7::])
    await state.set_state(AdminUpload.photo)
    await call.answer(cache_time=2)


@ad_route.message(AdminUpload.photo, F.photo)
async def ulpload_file_finish(msg: types.Message, state: FSMContext):
    await state.update_data(photo=msg.photo[-1].file_id)
    data = await state.get_data()
    await orm.upload_file(data)
    await bot.send_message(msg.from_user.id,
                           text=Texts.ADMIN_ADD_FILE,
                           reply_markup=kb.no_add)
    await state.set_state(AdminUpload.photo)


@ad_route.callback_query(F.data.startswith('change_'), Admin())
async def change_file_handler(call: types.CallbackQuery):
    query = await orm.get_files_admin(category=call.data[7::])
    for item in query:
        await bot.send_photo(call.from_user.id,
                             photo=item[0],
                             reply_markup=kb.admin_change_button(idx=item[1]))
    await call.answer(cache_time=2)


@ad_route.callback_query(F.data.startswith('idx_'), Admin())
async def change_file_start(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(call.from_user.id, text=Texts.ADMIN_CHANGE)
    await state.update_data(id=call.data[4::])
    await state.set_state(AdminChange.photo)
    await call.answer(cache_time=2)


@ad_route.message(AdminChange.photo, F.photo)
async def change_file_finish(msg: types.Message, state: FSMContext):
    await state.update_data(file=msg.photo[-1].file_id)
    data = await state.get_data()
    await orm.change_file_admin(data)
    await bot.send_message(msg.from_user.id,
                           text=Texts.ADMIN_SUCCESFUL, reply_markup=kb.admin_kb())
    await state.clear()


@ad_route.callback_query(F.data == 'no_add_admin')
async def no_add_call(call: types.CallbackQuery, state: FSMContext):
    """Хендлер отмены"""
    await state.clear()
    await call.message.edit_text(text='Галя,отменила 👌',
                                 reply_markup=kb.back_admin)
    await call.answer(cache_time=2)


@ad_route.callback_query(F.data == 'add_choise_tur')
async def add_choise_tur_handler(call: types.CallbackQuery):
    await call.message.edit_text(text=Texts.ADMIN_CATALOG,
                                 reply_markup=await kb.admin_choise_kb())
    await call.answer(cache_time=2)


@ad_route.callback_query(F.data == 'get_file', Admin())
async def get_file(call: types.CallbackQuery):
    data = await orm.get_file_by_admin()
    file = pd.DataFrame(data)
    file.to_excel(f"Актуальный список на {datetime.date.today()}.xlsx")
    document = types.FSInputFile(f"Актуальный список на {datetime.date.today()}.xlsx")
    await bot.send_document(call.from_user.id, document=document)
    os.remove(f"Актуальный список на {datetime.date.today()}.xlsx")


@ad_route.message(Command('superadmin'), SuperAdmin())
async def superadmin_handler(msg: types.Message):
    await bot.send_message(msg.from_user.id,
                           text=Texts.SUPERADMIN,
                           reply_markup=kb.super_admin_menu())


@ad_route.callback_query(F.data == 'show_admins', SuperAdmin())
async def show_admin_namdler(call: types.CallbackQuery):
    await call.message.edit_text(text=Texts.show_list(Admin_list),
                                 reply_markup=kb.super_admin_menu())
    await call.answer(cache_time=2)


@ad_route.callback_query(F.data == 'add_admin', SuperAdmin())
async def add_admin_handler(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(call.from_user.id,
                           text=Texts.SUPERADMIN_ADD_REMOVE,
                           reply_markup=kb.no_add)
    await state.set_state(AdminAdd.id_number)
    await call.answer(cache_time=2)


@ad_route.message(AdminAdd.id_number, SuperAdmin())
async def add_admin_finish(msg: types.Message, state: FSMContext):
    if msg.text.isdigit():
        Admin_list.append(int(msg.text))
        await bot.send_message(msg.from_user.id,
                               text=Texts.SUPERADMIN_SUCCES,
                               reply_markup=kb.super_admin_menu())
        await state.clear()
    else:
        await bot.send_message(msg.from_user.id,
                               text=Texts.SUPERADMIN_ERR)
        await state.set_state(AdminAdd.id_number)


@ad_route.callback_query(F.data == 'remove_admin', SuperAdmin())
async def remove_admin_handler(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(call.from_user.id,
                           text=Texts.SUPERADMIN_ADD_REMOVE,
                           reply_markup=kb.no_add)
    await state.set_state(AdminRemove.id_number)
    await call.answer(cache_time=2)


@ad_route.message(AdminRemove.id_number, SuperAdmin())
async def remove_admin_finish(msg: types.Message, state: FSMContext):
    if msg.text.isdigit():
        Admin_list.remove(int(msg.text))
        await bot.send_message(msg.from_user.id,
                               text=Texts.SUPERADMIN_SUCCES,
                               reply_markup=kb.super_admin_menu())
        await state.clear()
    else:
        await bot.send_message(msg.from_user.id,
                               text=Texts.SUPERADMIN_ERR)
        await state.set_state(AdminRemove.id_number)


@ad_route.callback_query(F.data == 'add_button', Admin())
async def add_button_handler(call: types.CallbackQuery):
    await call.message.edit_text(text=Texts.BUTTON_ADMIN,
                                 reply_markup=kb.admin_button_choise())
    await call.answer(cache_time=2)


@ad_route.callback_query(F.data.startswith('button_'), Admin())
async def button_choise_action(call: types.CallbackQuery, state: FSMContext):
    if call.data == "button_upload":
        await call.message.edit_text(text=Texts.BUTTON_SET_NAME,
                                     reply_markup=kb.no_add)
        await state.set_state(AdminButtonActionUpload.button_name)
        await call.answer(cache_time=2)
    elif call.data == 'button_change':
        button_list = await orm.get_categories()
        for i in button_list:
            await bot.send_message(call.from_user.id,
                                   text=Texts.button_choise(i[0]),
                                   reply_markup=kb.button_choise_kb(i[1]))
        await state.set_state(AdminButtonActionChange.button_idx)
        await bot.send_message(call.from_user.id, text=Texts.NO_ADD, reply_markup=kb.no_add)
        await call.answer(cache_time=2)
    elif call.data == 'button_delete':
        button_list = await orm.get_categories()
        for i in button_list:
            await bot.send_message(call.from_user.id,
                                   text=Texts.button_choise(i[0]),
                                   reply_markup=kb.button_delete_kb(i[1]))
        await bot.send_message(call.from_user.id, text=Texts.NO_ADD, reply_markup=kb.no_add)
        await state.set_state(AdminButtonActionDelete.button_idx)
        await call.answer(cache_time=2)


@ad_route.message(AdminButtonActionUpload.button_name, Admin())
async def admin_upload_button_finish(msg: types.Message, state: FSMContext):
    await orm.admin_add_button(data=msg.text)
    await bot.send_message(msg.from_user.id,
                           text=Texts.SUCC_ADD,
                           reply_markup=kb.back_admin)
    await state.clear()


@ad_route.callback_query(AdminButtonActionChange.button_idx,
                         F.data.startswith('changebutton_'),
                         Admin())
async def button_change_idx(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(button_idx=call.data[13::])
    await bot.send_message(chat_id=call.from_user.id, text=Texts.BUTTON_SET_NAME,
                           reply_markup=kb.no_add)
    await state.set_state(AdminButtonActionChange.button_name)
    await call.answer(cache_time=2)


@ad_route.message(AdminButtonActionChange.button_name, Admin())
async def admin_upload_button_finish(msg: types.Message, state: FSMContext):
    await state.update_data(button_name=msg.text)
    data = await state.get_data()
    await orm.admin_change_button(data=data)
    await bot.send_message(msg.from_user.id,
                           text=Texts.SUCC_ADD,
                           reply_markup=kb.back_admin)
    await state.clear()


@ad_route.callback_query(AdminButtonActionDelete.button_idx,
                         F.data.startswith('deletebutton_'),
                         Admin())
async def delete_button_finish(call: types.CallbackQuery, state: FSMContext):
    await orm.admin_delete_button(call.data[13::])
    await bot.send_message(call.from_user.id,
                           text=Texts.SUCC_ADD,
                           reply_markup=kb.back_admin)
    await state.clear()
    await call.answer(cache_time=2)


@ad_route.callback_query(F.data == 'add_visa', Admin())
async def add_visa_start(call: types.CallbackQuery):
    await call.message.edit_text(text=Texts.ADMIN_CATALOG_CHOISE,
                                 reply_markup=kb.admin_visa_choise())


@ad_route.callback_query(F.data == 'avisa_upload', Admin())
async def upload_visa(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(text=Texts.UPLOAD_VISA_START,
                                 reply_markup=kb.upload_visa_catalog())
    await state.set_state(AdminUploadVisa.visa_category)
    await call.answer(cache_time=2)


@ad_route.callback_query(AdminUploadVisa.visa_category,
                         F.data.startswith('uvisa_'),
                         Admin())
async def upload_visa_add_category(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(category=call.data[6::])
    await call.message.edit_text(text=Texts.ADMIN_ADD)
    await state.set_state(AdminUploadVisa.visa_photo_id)
    await call.answer(cache_time=2)


@ad_route.message(AdminUploadVisa.visa_photo_id, F.photo)
async def upload_visa_finish(msg: types.Message, state: FSMContext):
    await state.update_data(photo=msg.photo[-1].file_id)
    data = await state.get_data()
    await orm.upload_file(data)
    await bot.send_message(msg.from_user.id,
                           text=Texts.ADMIN_SUCCESFUL, reply_markup=kb.admin_kb())
    await state.clear()
