from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


lang_keyboard = ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton("π¬π§ EN"),
		KeyboardButton("π·πΊ RU"),
		KeyboardButton("πΊπΏ UZ")
		],
		[
		KeyboardButton("β¬οΈ Ortga")
		]	
	],
	resize_keyboard=True
)

only_langs = ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton("π¬π§ EN"),
		KeyboardButton("π·πΊ RU"),
		KeyboardButton("πΊπΏ UZ")
		]
	],
	resize_keyboard=True
)