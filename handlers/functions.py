import sqlite3
connect = sqlite3.connect("db/varzay.db")
cursor = connect.cursor()
def status_users(message_id):
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",
                                 (message_id,))
    user_status = cursor.fetchone()
    if user_status[0] == 'Rab':
        user_status2 = '<b>👑ГЛАВА☣️</b>'

    if user_status[0] == 'Zamchestera':
        user_status2 = '<b>💥ЗАМ-CHESTER🫶</b>'        

    if user_status[0] == 'Admin':
        user_status2 = '<b>👮ADMIN💕</b>'

    if user_status[0] == 'Player':
        user_status2 = '<b>✌️Игрок</b>'
    if user_status[0] == 'vip':
        user_status2 = '<b>⚡VIP</b>'
    if user_status[0] == 'premium':
        user_status2 = '<b>💎PREMIUM</b>'
    if user_status[0] == 'delux':
        user_status2 = '<b>💥DELUXE</b>'
    return user_status2



## Можете сравнить с корректным результатом, всё 1-в-1:
# result = 7 - math.sin(3.141592 * 0.75) + math.cos(2.718281)

