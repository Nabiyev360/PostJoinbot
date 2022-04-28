from aiogram.types import Message


from loader import dp
from keyboards.default.langKeyboard import lang_keyboard
from keyboards.default.mainKeyboard import main_keyboard

@dp.message_handler(text= "🇬🇧 Language | 🇷🇺 Язык | 🇺🇿 Til")
async def langs(msg: Message):
	await msg.answer("<b>Bot tilini tanlang:</b>", reply_markup=lang_keyboard)



@dp.message_handler(text= ['🇬🇧 EN', '🇷🇺 RU', '🇺🇿 UZ'])
async def choice_lang(msg: Message):
	if msg.text == '🇬🇧 EN':
		await msg.answer('<b>Main menu:</b>', reply_markup=main_keyboard('🌟 Favourites', '📃 Create post'))
	elif msg.text == '🇷🇺 RU':
		await msg.answer('<b>Главный меню:</b>', reply_markup=main_keyboard('🌟 Избранные', '📃 Создать пост'))
	elif msg.text == '🇺🇿 UZ':
		await msg.answer('<b>Asosiy menyu:</b>', reply_markup=main_keyboard())