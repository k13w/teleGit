from sys import path
path.append("src/")
from time import sleep
from GitApi import GitHub
import configparser
from telegram import ParseMode, Emoji
from telegram.ext import Updater, CommandHandler

# Bot Configuration
config = configparser.ConfigParser()
config.read_file(open('config.ini'))
# Connecting the telegram API
# Updater will take the information and dispatcher connect the message to
# the bot
up = Updater(token=config['DEFAULT']['token'])
dispatcher = up.dispatcher


# Home function
def start(bot, update):
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
def listing(bot, update, args):
    gh = GitHub()
    for user in args:
        bot.send_message(chat_id=update.message.chat_id,
                         text='{0} Listando os repositórios do usuário '
                         .format('\U0001F5C4') +
                         '[{0}](https://github.com/{0}) {1}'.format(
                             user, Emoji.WHITE_DOWN_POINTING_BACKHAND_INDEX),
                         parse_mode=ParseMode.MARKDOWN)

        bot.send_message(chat_id=update.message.chat_id,
                         text=gh.GetRepos(user))


# Function to display user information
def info(bot, update, args):
    gh = GitHub()
    for user in args:
        bot.send_message(chat_id=update.message.chat_id,
                         text='{2} Informações sobre o usuário ' +
                         '[{0}](https://github.com/{0}) {1}'.format(
                             user, Emoji.WHITE_DOWN_POINTING_BACKHAND_INDEX,
                             Emoji.INFORMATION_SOURCE),
                         parse_mode=ParseMode.MARKDOWN)
        bot.send_message(chat_id=update.message.chat_id,
                         text=gh.GetInfo(user))

# Add handlers to dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('listing', listing, pass_args=True))
dispatcher.add_handler(CommandHandler('info', info, pass_args=True))

# Start the program
up.start_polling()

# Developed by Heaven, Jr750ac, Pedro Souza, Israel Sant'Anna all rights
# reserved
