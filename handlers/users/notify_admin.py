from keyboards.inline.keyboards_inline import download
from file_service.get_file import get_files
from aiogram.types import CallbackQuery
from loader import dp


@dp.callback_query_handler(lambda call: call.data == "download")
async def send_message(call: CallbackQuery):
    with open(await get_files(), "rb") as file:
        await call.message.answer_document(file)
    await call.message.answer("Tanlov ishtirokchilari ruyxatini yuklab olish tugmasini bosing!", reply_markup=download)
