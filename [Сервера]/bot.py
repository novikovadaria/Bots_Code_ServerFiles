import telebot
from telebot import types
import requests
import lxml.html
import datetime
import math
import datetime

bot_token = '5621377945:AAEcFz1VLF34rjIYZVj14WkHEk64V2Kq1z4'
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Здравствуй, <b>{message.from_user.first_name} </b>!'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['work'])
def start(message):
    mesg = bot.send_message(
        message.chat.id, 'Напиши своё имя и общее число символов, с которым ты работал(а) через слеш. Например, Даша/12.452.')
    bot.register_next_step_handler(mesg, answer)


def answer(message):
    l_i = list(message.text)
    l = len(l_i)
    ind = l_i.index('/')
    name = []
    symbols = []
    for i in l_i[0:ind]:
        name.append(i)

    for i in l_i[ind+1:l]:
        symbols.append(i)

    s_part = ''.join(name)
    s_symbols = ''.join(symbols)
    part = s_part.replace(' ', '-')
    amoubt_symb = s_symbols.replace(' ', '-')
    integ = float(amoubt_symb)
    ceiled_num = math.ceil(integ)
    money = ceiled_num * 10
    with open('pay.csv', 'a', encoding='utf-8') as file:
        file.write(
            f'\n\nДата внесения данных: {datetime.datetime.now()}\nУчастник: {part}\nКол-во символов: {amoubt_symb}\nСуммарное число выплаты: {money}\n****\n')
    output = f'Сумма выплаты за данное количество символов составляет {money} ₽.\nДанные записаны, спасибо! 😌'
    bot.send_message(message.chat.id, output)


bot.polling()
