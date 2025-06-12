import os
from dotenv import load_dotenv
import telebot
import threading

load_dotenv()

bot_instance = telebot.TeleBot(os.getenv("TELEGRAM_BOT_KEY"))

class TelebotManager:
    def __init__(self):
      self.bot = bot_instance
    
    @bot_instance.message_handler(commands=['start', 'help'])
    def cmd(message):
      #  bot.reply_to(message, "Howdy, how are you doing?")
      # self.bot.send_message(message.chat.id, "This is a cmd.")
      pass


    def send_message(self, telegram_message):
      bot_response = None
      
      @bot_instance.message_handler(content_types=['text'])
      def send_bot_message():
         response = self.bot.send_message(telegram_message.chat_id, telegram_message.content)
         return response
         
         # self.bot.send_message(message.chat.id, "Normal message.")
         # #  print(message.chat.id)
         # if message.chat.username == 'james_bond007':
         #    if 'text to search' in message.text:
         #       self.bot.send_message(message.chat.id, "Oki doki.")
         #       # bot.send_message(message.chat.id, "Hello, Agent.")

      bot_response = send_bot_message()
      return bot_response

    def start_bot(self):
      self.bot.infinity_polling()

telegram_bot = TelebotManager()

# creates a thread to run the pooling bot
polling_thread = threading.Thread(target=telegram_bot.start_bot)
polling_thread.start()