from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard(favourites='π Saralanganlar', create= 'π Post yaratish'):
	keyboard = ReplyKeyboardMarkup(
		keyboard=[
			[
				KeyboardButton(favourites),
				KeyboardButton(create)
			],
			[
				KeyboardButton("π¬π§ Language | π·πΊ Π―Π·ΡΠΊ | πΊπΏ Til")
			]
		],
		resize_keyboard=True
	)

	return keyboard