from config import *
import random
import telebot

bot = telebot.TeleBot(TOKEN)

badlinks = ['https://www.youtube.com/channel/UCXlqFQmZZOb78teSnAqhuwA', 
            'https://www.youtube.com/channel/UCLkAepWjdylmXSltofFvsYQ', 
            'https://www.youtube.com/channel/UC3jOd7GUMhpgJRBhiLzuLsg'
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am testBot 101.
I am here to do nothing.\
""")

@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)
    
@bot.message_handler(commands=['help'])
def send_nohelp(message):
    bot.reply_to(message, """\
There will be no help, lol.\
""")

@bot.message_handler(commands=['detour'])
def detour_random(message):
    detoursong = (["detour", "dtla", "i like ur look", "check it", "polo", "brutalist", "need for speed", "jeep", "101", "basketball", "freak it", "pop sound"])
    bot.reply_to(message, random.choise(detoursong))

@bot.message_handler(func=lambda message: message.text and any(link in message.text for link in badlinks))
def flops_aftermath(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    try:
        bot.delete_message(chat_id, message.message_id)
        bot.ban_chat_member(chat_id, user_id)
        bot.send_message(chat_id, f"Banned {user_id} for listening to flops.")
    except Exception as e:
        print(f"error")

        
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()