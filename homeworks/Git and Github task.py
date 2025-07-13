import os
from datetime import datetime
import telebot

TOKEN = os.getenv('TG_TOKEN')

bot = telebot.TeleBot(TOKEN)

user_data = {}

COMMAND_START = 'start'
COMMAND_SLEEP = 'sleep'
COMMAND_WAKE = 'wake'
COMMAND_QUALITY = 'quality'
COMMAND_NOTES = 'notes'

@bot.message_handler(commands=[COMMAND_START])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я буду помогать тебе отслеживать параметры сна. Используй команды /sleep, /wake, /quality, /notes.')

@bot.message_handler(commands=[COMMAND_SLEEP])
def sleep(message):
    user_id = str(message.from_user.id)
    if user_id in user_data and 'start_time' in user_data[user_id]:
        bot.send_message(message.chat.id, 'Ты уже отправил время отхода ко сну. Используй команду /wake, чтобы завершить.')
    else:
        user_data[user_id] = {'start_time': datetime.now()}
        bot.send_message(message.chat.id, 'Спокойной ночи! Не забудь сообщить мне, когда проснешься командой /wake')

@bot.message_handler(commands=[COMMAND_WAKE])
def wake(message):
    user_id = str(message.from_user.id)
    start = user_data[user_id]['start_time']
    end = datetime.now()
    user_duration = (end - start).total_seconds()/3600
    user_data[user_id]['duration'] = user_duration
    bot.send_message(message.chat.id, f'Доброе утро! Ты проспал около {user_duration:.6f} часов. Не забудь оценить качество сна командой /quality и оставить заметки командой /notes.')

@bot.message_handler(commands=[COMMAND_QUALITY])
def quality(message):
    user_id = str(message.from_user.id)
    user_quality = message.text[len(COMMAND_QUALITY):]
    user_data[user_id]['quality'] = user_quality
    bot.send_message(message.chat.id, 'Спасибо за оценку качества сна!')

@bot.message_handler(commands=[COMMAND_NOTES])
def notes(message):
    user_id = str(message.from_user.id)
    user_notes = message.text[len(COMMAND_NOTES):]
    user_data[user_id]['notes'] = user_notes
    bot.send_message(message.chat.id, 'Заметка успешно сохранена!')

bot.polling(none_stop = True)