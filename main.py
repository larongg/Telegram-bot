from config import TOKEN
import telebot
from telebot import types


bot = telebot.TeleBot(TOKEN)
surnames = ['Шестопалов', 'Титов', 'Франциско',
            'Клюшнева', 'Калмыкова', 'Брюханова',
            'Мещеряков', 'Гензе', 'Александренко',
            'Федотов', 'Ерзумашев', 'Замуруева',
            'Никитин', 'Худков', 'Миронова',
            'Плешивцев', 'Мальцева', 'Сальцов',
            'Шкуратецкий', 'Наконечный', 'Басманова',
            'Славкин', 'Казаков', 'Курганский',
            'Елистратов', 'Ильичёв', 'Цыганова',
            'Лейман', 'Кузьмин', 'Шаматов',
            'Тагаров', 'Гончаров',]
surnames.sort()


@bot.message_handler(commands=['start'])
def get_sur(message):
    global surnames
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for surname in surnames:
        markup_reply.add(types.KeyboardButton(surname))
    bot.send_message(message.chat.id, 'Выберите фамилию', reply_markup=markup_reply)

@bot.message_handler(content_types = ['text'])
def get_text(message):
    global surnames
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text in surnames:
        markup_reply.add(types.KeyboardButton('Присутствую'),
                         types.KeyboardButton('Болею'),
                         types.KeyboardButton('Опаздываю'),
                         types.KeyboardButton('Отсутствую по уважительной причине'),
                         types.KeyboardButton('Не приду'))
        bot.send_message(message.chat.id, 'Ты на паре?' ,reply_markup=markup_reply)
    else:
        bot.send_message(message.chat.id, '/start')


bot.polling(none_stop=True, interval=0)