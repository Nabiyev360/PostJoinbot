from aiogram import types

from loader import dp
from keyboards.default.mainKeyboard import main_keyboard


back_dict = {
    '⬅️ Ortga':['Asosiy menyu:', '🌟 Saralanganlar', '📃 Post yaratish'],
    '⬅️ Назад':['Главный меню:', '🌟 Избранные', '📃 Создать пост'],
    '⬅️ Back': ['Main menu:', '🌟 Favourites', '📃 Create post']
}

@dp.message_handler(text = back_dict)
async def backer(msg: types.Message):
    await msg.answer(text = f"<b>{back_dict[msg.text][0]}</b>", 
        reply_markup=main_keyboard(back_dict[msg.text][1], back_dict[msg.text][2]))