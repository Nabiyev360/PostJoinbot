from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def type_keyboard(text, photo, gif, video, back):
	keyboard = ReplyKeyboardMarkup(
		keyboard=[
			[
			KeyboardButton(text),
			KeyboardButton(photo)
			],
			[
			KeyboardButton(gif),
			KeyboardButton(video),
			],
			[
			KeyboardButton(back)
			]
		],
		resize_keyboard=True
	)

	return keyboard