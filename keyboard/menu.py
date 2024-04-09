from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
help_menu = InlineKeyboardMarkup()
main = InlineKeyboardButton(text='💡', callback_data='main')
main1 = InlineKeyboardButton(text='🏚️', callback_data='main1')
games = InlineKeyboardButton(text='🎮', callback_data='games')
entertainment = InlineKeyboardButton(
    text='🤘', callback_data='entertainment')
clans=InlineKeyboardButton(text='⚔️', callback_data='clans')
city = InlineKeyboardButton(text='🏙', callback_data='city')
addb = InlineKeyboardButton(
    text='Добавить бота 😄', url='https://t.me/varzay_bot?startgroup=true') #не работает-addb
help_menu.add(main, main1, games, entertainment, clans, city,)
help_back = InlineKeyboardMarkup(row_width=2)
main1 = InlineKeyboardButton(text='⬅️ Назад', callback_data='back')
help_back.add(main1)

help_topback = InlineKeyboardMarkup(row_width=2)
main1 = InlineKeyboardButton(text='⬅️ Назад', callback_data='backtop')
help_topback.add(main1)
def list_clans_get(count):
    list_clans = InlineKeyboardMarkup(row_width=3)
    list_clans2 = InlineKeyboardButton(text=' 📝 Список кланов', callback_data=f'clans_list_{count}')
    list_clans.add(list_clans2)
    return list_clans
def list_clans_get2(count,ishave=True):
    list_clans = InlineKeyboardMarkup(row_width=3)
    if count>=10 and ishave==True:
        list_clans2 = InlineKeyboardButton(text=' Назад', callback_data=f'clans_list_{count-10}')
        list_clans3 = InlineKeyboardButton(text=' Дальше', callback_data=f'clans_list_{count+10}')
        list_clans.add(list_clans2,list_clans3)
    elif count<10 and ishave==True:
        list_clans3 = InlineKeyboardButton(text=' Дальше', callback_data=f'clans_list_{count+10}')
        list_clans.add( list_clans3)
    elif ishave==False:
        list_clans2 = InlineKeyboardButton(text=' Назад', callback_data=f'clans_list_{count - 10}')
        list_clans.add(list_clans2)
    return list_clans

