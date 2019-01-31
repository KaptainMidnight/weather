import requests
from bs4 import BeautifulSoup
from telegram.ext import *

updater = Updater(token="789590935:AAGE_s_bcGa0JMfNbbFqScMFiXl2Z8t6roc")
dispatcher = updater.dispatcher

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello, I am bot for weather")


def textMessage(bot, update):
    try:
        response = update.message.text
        s = requests.get("https://sinoptik.com.ru/погода-" + str(response))
        soup = BeautifulSoup(s.text, "html.parser")
        p1 = soup.select('.temperature .p1')  # Night
        weather1 = p1[0].getText()
        p2 = soup.select('.temperature .p2')  # Night
        weather2 = p2[0].getText()
        p3 = soup.select('.temperature .p3')  # Morning
        weather3 = p3[0].getText()
        p4 = soup.select('.temperature .p4')  # Morning
        weather4 = p4[0].getText()
        p5 = soup.select('.temperature .p5')  # Day
        weather5 = p5[0].getText()
        p6 = soup.select('.temperature .p6')  # Day
        weather6 = p6[0].getText()
        p7 = soup.select('.temperature .p7')  # Evening
        weather7 = p7[0].getText()
        p8 = soup.select('.temperature .p8')  # Evening
        weather8 = p8[0].getText()
        discription = soup.select('.wDescription .rSide')
        discription1 = discription[0].getText()
        night = "Ночью: " + str(weather1) + " " + str(weather2)
        morning = "Утром: " + str(weather3) + " " + str(weather4)
        day = "Днем: " + str(weather5) + " " + str(weather6)
        evening = "Вечером: " + str(weather7) + " " + str(weather8)
        bot.send_message(chat_id=update.message.chat_id, text=night)
        bot.send_message(chat_id=update.message.chat_id, text=morning)
        bot.send_message(chat_id=update.message.chat_id, text=day)
        bot.send_message(chat_id=update.message.chat_id, text=evening)
        bot.send_message(chat_id=update.message.chat_id, text=discription1)
    except:
        bot.send_message(chat_id=update.message.chat_id, text="Город введен не верно!")


start_command_handler = CommandHandler("start", startCommand)
text_message = MessageHandler(Filters.text, textMessage)
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message)
updater.start_polling(clean=True)
updater.idle()
