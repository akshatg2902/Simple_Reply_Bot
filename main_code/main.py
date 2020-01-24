# A simple reply bot using the decorator mechanism.
# It Reply back any incoming text messages.

import telebot

API_TOKEN = '1053241974:AAF-7QLRcwr95h55KFVngYslDP1pwFWLBiE'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am Simple Reply Bot.
I am here to Reply your kind words back to you. Just say anything nice and I'll say the exact same thing to you!
isn't it exciting\
""")
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """\
HEY! THIS IS HELP SECTION.
To use this bot,send it as a username\
""")

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.polling()
