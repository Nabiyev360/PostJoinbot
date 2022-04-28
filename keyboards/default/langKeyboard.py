from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


lang_keyboard = ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton("🇬🇧 EN"),
		KeyboardButton("🇷🇺 RU"),
		KeyboardButton("🇺🇿 UZ")
		],
		[
		KeyboardButton("⬅️ Ortga")
		]	
	],
	resize_keyboard=True
)

only_langs = ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton("🇬🇧 EN"),
		KeyboardButton("🇷🇺 RU"),
		KeyboardButton("🇺🇿 UZ")
		]
	],
	resize_keyboard=True
)