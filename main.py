
from GitApi import GitHub
import configparser
from telegram.ext import Updater, CommandHandler

# Configuração do Bot
config = configparser.ConfigParser()
config.read_file(open('config.ini'))

# Conectando a API do telegram
# Updater pegará as informações e dispatcher conectará a mensagem ao bot
up = Updater(token=config['DEFAULT']['token'])
dispatcher = up.dispatcher

# Função Inicial


def start(bot, update):
    me = bot.get_me()

    # Mesagem Inicial
    msg = "Bem vindo!\n"
    msg += "Eu sou o TeleGit\n"
    msg += "O que você gostaria de fazer?\n"
    msg += "/listing +username - Listará seus repositórios\n"
    msg += "Ex: /listing HeavenH"

    # Envia a mensagem com o menu
    bot.send_message(chat_id=update.message.chat_id, text=msg)

# Função para listar os repositórios


def listing(bot, update):
    user = update.message.text.split()[1]
    bot.send_message(chat_id=update.message.chat_id, text=user)
    re = GitHub()
    bot.send_message(chat_id=update.message.chat_id,
                     text=re.GetRepos(user))


def info(bot, update):
    user = update.message.text.split()[1]
    bot.send_message(chat_id=update.message.chat_id, text=user)
    msg = GitHub()
    bot.send_message(chat_id=update.message.chat_id, text=msg.GetInfo(user))

# Transforma as funções em Comandos
start_handler = CommandHandler('start', start)
listing_handler = CommandHandler('listing', listing)
info_handler = CommandHandler('info', info)

# Envia os Comandos para o telegram
dispatcher.add_handler(start_handler)
dispatcher.add_handler(listing_handler)
dispatcher.add_handler(info_handler)

# Desenvolvido by Heaven,CliTrix,Cerberu5 all rights reserved
