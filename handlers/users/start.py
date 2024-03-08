from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.keyboards_inline import keyboard, download
from data.config import ADMINS, ADMIN

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n Xush kelibsiz “Rangtasvir asarlari” nomli bolalar rasmlar tanloviga ishtirok etish uchun ruyhatdan o'tish botiga.")
    await message.answer(
        "Tanlov ishtirokchilari ruyxatini yuklab olish tugmasini bosing!" if str(message.from_user.id) in (
            str(ADMINS), str(ADMIN)) else "Tanlovda ishtirok etish uchun telegram raqamingizni yuboring!",
        reply_markup=download if str(message.from_user.id) in (str(ADMINS), str(ADMIN)) else keyboard)
