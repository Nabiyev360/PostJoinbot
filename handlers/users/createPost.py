from aiogram.types import Message


from loader import dp
from keyboards.default.postTypeKeyboard import type_keyboard

post_dict = {
	'📃 Post yaratish':['Post turini tanlang:', 'Tekst', 'Rasm', 'Gif', 'Video', '⬅️ Ortga'],
	'📃 Создать пост':['Выберите тип поста:', 'Текст', 'Картинка', 'GIF', 'Видео', '⬅️ Назад'], 
	'📃 Create post': ['Select type of post:', 'Text', 'Photo', 'GIF', 'Video', '⬅️ Back']
}

@dp.message_handler(text= post_dict)
async def create_handler(msg: Message):
	await msg.answer(text = f"<b>{post_dict[msg.text][0]}</b>", 
		reply_markup=type_keyboard(post_dict[msg.text][1], post_dict[msg.text][2] , post_dict[msg.text][3], post_dict[msg.text][4], post_dict[msg.text][5]))