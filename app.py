import os
from flask import Flask,render_template,request,redirect
import time
import threading
import telebot


TOKEN = '5072766021:AAHN57wjgpEG1c6OSqoMeYXbRBdbeGgElYs'
bot = telebot.TeleBot(TOKEN)
#app=Flask(__name__)
server = Flask(__name__)

 
@bot.message_handler(commands=['start'])
def start(message):
  bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

def akhil():
  while True:
    bot.send_message(chat_id="685472615",text="running🌜")
    print("akhil")
    print("kyu")
    time.sleep(10)

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200
 
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://' + 'alivebots' + '.onrender.com/' + f"{TOKEN}")
    return "!", 200

@server.route('/home')
def getMessage():
  return("running")

if __name__ == "__main__":
  threading.Thread(target=akhil, name='run_server_time', daemon=True).start()
  #server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
  #server.run(debug=True,host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))
  server.run(debug=True,host="0.0.0.0", port=int(os.environ.get('PORT', 1000)))

