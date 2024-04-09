from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

gamevbmenu = InlineKeyboardMarkup(row_width=1)
gamevb = InlineKeyboardButton(text='ИГРАТЬ 🎮', callback_data='gamevb')
gamevbmenu.add(gamevb)

help_perexod = InlineKeyboardMarkup(row_width=2)
addb = InlineKeyboardButton(
    text='Переход в лс 😄', url='https://t.me/varzay_bot')

help_perexod.add(addb)
help_donat = InlineKeyboardMarkup(row_width=3)

donat1 = InlineKeyboardButton(text='⭐️', callback_data='donat1')
donat2 = InlineKeyboardButton(text='💎 ', callback_data='donat2')
donat3 = InlineKeyboardButton(text='🔥 ', callback_data='donat3')
donat4 = InlineKeyboardButton(text='👮‍♂️ ', callback_data='donat4')
donat5 = InlineKeyboardButton(text='💸 ', callback_data='donat5')
donat6 = InlineKeyboardButton(text='Прочее 📁', callback_data='donat6')
donat7 = InlineKeyboardButton(text='Пополнить 🍩', callback_data='donat7')
help_donat.add(donat1, donat2, donat3, donat4, donat5,donat6,donat7)

help_top = InlineKeyboardMarkup(row_width=2)
topb = InlineKeyboardButton(text='💸 Баланс', callback_data='topb')
tope = InlineKeyboardButton(text='💡 Опыт', callback_data='tope') #выключен
topg = InlineKeyboardButton(text='🎮 Игры', callback_data='topg')#выключен
toppet = InlineKeyboardButton(text='🤼 Бои ', callback_data='toppet')#выключен
top_clan=InlineKeyboardButton(text='⚔️Кланы', callback_data='top_clan')
top_city = InlineKeyboardButton(text='🌆 Города', callback_data='top_city')
help_top.add(topb,top_clan,top_city)

help_invite = InlineKeyboardMarkup(row_width=2)
addb = InlineKeyboardButton(
    text='Добавить бота 😄', url='https://t.me/varzay_bot?startgroup=true')

help_invite.add(addb)
help_bonus = InlineKeyboardMarkup(row_width=3)
bonus = InlineKeyboardButton(text='🎁 Бoнус ', callback_data='bonus1')
main1 = InlineKeyboardButton(text='📰 Канал бота', url='https://t.me/varzay_channel')
help_bonus.add(main1) #что бы убрать бонус с баланса надо help_bonus.add() написать вот так

help_bonus2 = InlineKeyboardMarkup(row_width=1)
simple_bonus = InlineKeyboardButton(text='🎁 Бoнус ', callback_data='bonus1')
vip_bonus = InlineKeyboardButton(text='⭐️ VIP Бoнус', callback_data='bonus2')
prem_bonus = InlineKeyboardButton(text='💎 PREMIUM Бoнус ', callback_data='bonus3')
delux_bonus = InlineKeyboardButton(text='🔥 DELUX Бoнус ', callback_data='bonus4')
help_bonus2.add(simple_bonus,vip_bonus,prem_bonus,delux_bonus)
def unmute_kb(user_id: int):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton(text='🔗 Размутить', callback_data=f'unmute_{user_id}'))
    return kb


def unban_kb(user_id: int):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton(text='🔗 Разбанить', callback_data=f'unban_{user_id}'))
    return kb

help_bonus3 = InlineKeyboardMarkup(row_width=1)
moderatia = InlineKeyboardButton(text='🛠', callback_data='moderatia')
help_bonus3.add(moderatia)


panelowner1 = InlineKeyboardMarkup(row_width=1)
panelowner = InlineKeyboardButton(text='🛠', callback_data='panelowner')
panelowner1.add(panelowner)