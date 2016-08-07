import telegram
import configparser
from requests import get

from telegram.ext import Updater, CommandHandler

#Configuração do Bot
config = configparser.ConfigParser()
config.read_file(open('config.ini'))

#Conectando a API do telegram
#Updater pegará as informações e dispatcher conectará a mensagem ao bot
updater = Updater(token=config['DEFAULT']['token'])
dispatcher = updater.dispatcher

def start(bot, update):
	me = bot.get_me()

	#Mesagem Inicial
	msg = "Bem vindo!\n"
	msg += "Eu sou o TeleGit\n"
	msg += "O que você gostaria de fazer?\n"
	msg += "/listing - Listará seus repositórios"

	#Comandos Menu
	main_menu_keyboad = [[telegram.KeyboardButton('/listing')]]
	reply_kb_markup = telegram.ReplyKeyboardMarkup(main_menu_keyboad,resize_keyboard=True,one_time_keyboard=True)

	#Envia a mensagem com o menu
	bot.send_message(chat_id=update.message.chat_id,text=msg,reply_markup=reply_kb_markup)

def listing(bot, update):
	r = get('https://api.github.com/users/')
	#Listará os repositórios do github do usuário
	bot.send_message(chat_id=update.message.chat_id,text="Listando seu github :)")

#ComandHandler Tranformara a função start em comando
#dispatcher Enviaraa a função em comando para o telegram	

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
listing_handler = CommandHandler('listing', listing)
dispatcher.add_handler(listing_handler)