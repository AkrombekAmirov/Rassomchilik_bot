from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

button = KeyboardButton(text="📞 Telefon raqamingizni yuboring", request_contact=True)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard.add(button)
response_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="✅ XA", callback_data="1"),
    ],
    [
        InlineKeyboardButton(text="❌ YO'Q", callback_data="2"),
    ]
])
download = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="📥 Yuklab olish", callback_data="download"),
    ]
])
