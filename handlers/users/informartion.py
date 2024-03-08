from keyboards.inline import response_keyboard
from file_service.file_write import file_read
from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp
from states import *


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message, state: FSMContext):
    await state.update_data({"number": message.contact.phone_number})
    await message.answer("Familiya, Ism va sharifingizni kiriting.\nLotin alifbosida yozing.")
    await Person.number.set()


@dp.message_handler(state=Person.number)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data({"name": message.text})
    await message.answer("Siz bilan bog'lanish uchun telifon raqamingizni kiriting.")
    await Person.next()


@dp.message_handler(state=Person.name)
async def get_number(message: types.Message, state: FSMContext):
    await state.update_data({"set_number": message.text})
    data = await state.get_data()
    await message.answer(f"Raqamingiz: {data.get('number')}\n"
                         f"Familiya, Ism va sharifingiz: {data.get('name')}\n"
                         f"Telifon raqamingiz: {data.get('number')}", reply_markup=response_keyboard)
    await Person.next()


@dp.callback_query_handler(lambda call: call.data in ["1", "2"], state=Person.set_number)
async def get_response(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"status": call.data})
    data = await state.get_data()
    if data.get("status") == "1":
        await call.message.answer("Ma'lumotingiz qabul qilindi.")
        await file_read(data=[[f"{data.get('name')}", f"{data.get('number')}", f"{call.from_user.username}",
                               f"{data.get('set_number')}"]])
        await call.message.delete()
    else:
        await call.message.delete()
        await call.message.answer("Familiya, Ism va sharifingizni kiriting.\nLotin alifbosida yozing.")
        await Person.number.set()
