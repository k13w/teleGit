#!/usr/bin/env python
# -*- coding:utf-8 -*-


import configparser
from requests import get
from json import loads

from telegram.ext import Updater, CommandHandler

# Configuração do Bot
config = configparser.ConfigParser()
config.read_file(open('config.ini'))

# Conectando a API do telegram
# Updater pegará as informações e dispatcher conectará a mensagem ao bot
updater = Updater(token=config['DEFAULT']['token'])
dispatcher = updater.dispatcher

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
    r = get('https://api.github.com/users/' + user + '/repos').text
    r = loads(r)
    for repo in range(len(r)):
        bot.send_message(chat_id=update.message.chat_id,
                         text=r[repo]['html_url'])


# Transforma as funções em Comandos
start_handler = CommandHandler('start', start)
listing_handler = CommandHandler('listing', listing)

# Envia os Comandos para o telegram
dispatcher.add_handler(start_handler)
dispatcher.add_handler(listing_handler)

# Desenvolvido by Heaven,Jr750Ac,Pedro-Souza all rights reserved
