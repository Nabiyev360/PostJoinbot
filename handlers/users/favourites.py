from aiogram.types import Message


from loader import dp


favs = {
	'🌟 Favourites': "You don't have favorite posts",
	'🌟 Избранные': 'У вас нет избранных постов.',
	'🌟 Saralanganlar': "Sizda saqlangan postlar yo`q."}

@dp.message_handler(text= favs)
async def favorites_handler(msg: Message):	
	await msg.answer(f"<b>{favs[msg.text]}</b>")