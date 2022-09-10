from config import TOKEN, surnames, array, admins_id#, variants
import telebot
from telebot import types


bot = telebot.TeleBot(TOKEN)
#global variants
global surnames
global array
global admins_id


@bot.message_handler(commands=['start'])
def start(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for surname in surnames:
        markup_reply.add(types.KeyboardButton(surname))
    bot.send_message(message.chat.id, 'Выберите фамилию', reply_markup=markup_reply)


@bot.message_handler(commands=['getinfoadmin'])
def get_info_admin(message):
    if message.chat.id in admins_id:
        spisok = 'Список 8К23:'
        for people in array.keys():
            spisok += '\n' + str(array.get(people))
            '''for hzuzechepridumat in array.get(people):
                spisok += hzuzechepridumat + '\n' '''
        bot.send_message(message.chat.id, spisok)
    else:
        bot.send_message(message.chat.id, 'У вас нет прав')


@bot.message_handler(commands=['clear'])
def clear_spisok(message):
    if message.chat.id in admins_id:
        array.clear()
        bot.send_message(message.chat.id, 'Список очищен')
    else:
        bot.send_message(message.chat.id, 'У вас нет прав')


@bot.message_handler(content_types = ['text'])
def get_text(message):
    #markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text in surnames:
        array[str(message.chat.id)] = message.text
        bot.send_message(message.chat.id, 'Записал')
        '''for variant in variants:
            markup_reply.add(types.KeyboardButton(variant))
        bot.send_message(message.chat.id, 'Ты на паре?' ,reply_markup=markup_reply)
        array[str(message.chat.id)].append(message.text)
    elif message.text in variants:
        if message.text == 'Присутствую': bot.send_message(message.chat.id, 'Записал')
        elif message.text == 'Опаздываю': bot.send_message(message.chat.id, 'Как придёшь запишу')
        elif message.text == 'Отсутствую по уважительной причине': bot.send_message(message.chat.id, '@shestikpetr причину написать')
        elif message.text == 'Не приду': bot.send_message(message.chat.id, 'Дело твоё...')
        array[str(message.chat.id)].append(message.text)'''
    else:
        bot.send_message(message.chat.id, '/start')


bot.polling(none_stop=True, interval=0)