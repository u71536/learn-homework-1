"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


# PROXY = {
#     'proxy_url': 'socks5://t1.learn.python.ru:1080',
#     'urllib3_proxy_kwargs': {
#         'username': 'learn',
#         'password': 'python'
#     }
# }



def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Moon', 'Saturn', 'Uranus', 'Jupetir', 'Pluto']

def planet_name(update, context):
    user_text = update.message.text.split()
    planet_name = user_text[-1]
    if planet_name in planets:
        result = getattr(ephem, planet_name)
        constellation = ephem.constellation(result((datetime.datetime.now())))
        update.message.reply_text(constellation)
    else:
        update.message.reply_text("Вы не указали планету! Попробуйте снова")

def main():
    mybot = Updater("7197423506:AAGjCWp_Mtw7bMaIsO7ibeGgOiX6IpvH-Hw", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_name))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
