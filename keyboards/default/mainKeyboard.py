from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard(favourites='🌟 Saralanganlar', create= '📃 Post yaratish'):
	keyboard = ReplyKeyboardMarkup(
		keyboard=[
			[
				KeyboardButton(favourites),
				KeyboardButton(create)
			],
			[
				KeyboardButton("🇬🇧 Language | 🇷🇺 Язык | 🇺🇿 Til")
			]
		],
		resize_keyboard=True
	)

	return keyboard