from aiogram import types

apanel2 = types.InlineKeyboardMarkup(row_width=3)
apanel2.add(types.InlineKeyboardButton(text='💎 Восстановить роль "Владельца"', callback_data='owner'))
apanel2.add(types.InlineKeyboardButton(text='👑 Скачать базу данных', callback_data='getdb'))
apanel2.add(types.InlineKeyboardButton(text='👑 Структура бд', callback_data='baza'))

back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back.add(types.KeyboardButton('Отмена'))