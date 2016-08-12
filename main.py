from sys import path
path.append("src/")
from GitApi import GitHub
import configparser
from telegram.ext import Updater, CommandHandler

# Bot Configuration
config = configparser.ConfigParser()
config.read_file(open('config.ini'))

# Connecting the telegram API
# Updater will take the information and dispatcher connect the message to the bot
up = Updater(token=config['DEFAULT']['token'])
dispatcher = up.dispatcher

# Home function

def start(bot, update):
    me = bot.get_me()

    # Home message
    msg = "Bem vindo!\n"
    msg += "Eu sou o TeleGit\n"
    msg += "O que você gostaria de fazer?\n"
    msg += "/listing + username - Listará seus repositórios\n"
    msg += "/info + username - Listará suas informações\n"
    msg += "Ex: /listing HeavenH | /info HeavenH"

    # Send the message
    bot.send_message(chat_id=update.message.chat_id, text=msg)

# Function to list the repositories

def listing(bot, update):
    user = update.message.text.split()[1]
    bot.send_message(chat_id=update.message.chat_id, text=user)
    re = GitHub()
    bot.send_message(chat_id=update.message.chat_id,
                     text=re.GetRepos(user))

# Function to display user information

def info(bot, update):
    user = update.message.text.split()[1]
    bot.send_message(chat_id=update.message.chat_id, text=user)
    msg = GitHub()
    bot.send_message(chat_id=update.message.chat_id, text=msg.GetInfo(user))

# Transforms functions in Commands
start_handler = CommandHandler('start', start)
listing_handler = CommandHandler('listing', listing)
info_handler = CommandHandler('info', info)

# Sends the commands to the telegram
dispatcher.add_handler(start_handler)
dispatcher.add_handler(listing_handler)
dispatcher.add_handler(info_handler)

# Start the program
up.start_polling()

# Developed by Heaven, Jr750ac, Pedro Souza all rights reserved
