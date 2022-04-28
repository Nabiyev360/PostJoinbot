from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default.langKeyboard import only_langs


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        text = f"Salom {message.from_user.full_name}!\n\nXabarlar yaratishni boshlashdan oldin, quyidagi til sozlamalari tugmachasini bosib, tilingizni tanlang.",
        reply_markup=only_langs)