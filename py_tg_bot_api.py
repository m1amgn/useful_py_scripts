# Telegram Bot
# pip install pyTelegramBotAPI

import telebot

bot = telebot.TeleBot('YOUR TOKEN')

# send message
bot.send_message(chat_id='YOUR ID', text='Medium.com')

# send photo
bot.send_photo(chat_id='YOUR ID', photo=open('photo.jpg', 'rb'))

# send audio
bot.send_audio(chat_id='YOUR ID', audio=open('audio.mp3', 'rb'))

# send document
bot.send_document(chat_id='YOUR ID', document=open('document.pdf', 'rb'))

# send video
bot.send_video(chat_id='YOUR ID', video=open('video.mp4', 'rb'))

# Reply handler
@bot.message_handler(commands=['start', 'about', 'help'])
def send_welcome(msg):
    bot.reply_to(msg, "Welcome")

# Reply all Handler
@bot.message_handler(func=lambda msg: True)
def echo_all(msg):
    bot.reply_to(msg, msg.text)

# Ban Member handler
@bot.message_handler(commands=['ban'])
def ban_member(msg):
    bot.kick_chat_member(chat_id=msg.chat.id, user_id=msg.from_user.id)
    bot.reply_to(msg, "You have been banned")bot.infinity_polling()
