#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sys import path
from configparser import ConfigParser
from telegram import ParseMode, Emoji
from telegram.ext import Updater, CommandHandler
path.append("src/")
from GitApi import GitHub

# Bot Configuration
config = ConfigParser()
config.read_file(open('config.ini'))

# Connecting the telegram API
# Updater will take the information and dispatcher connect the message to
# the bot
up = Updater(token=config['DEFAULT']['token'])
dispatcher = up.dispatcher


# Home function
def start(bot, update):
    # Home message
    msg = "Hello {user_name}! I'm {bot_name}. \n"
    msg += "What would you like to do? \n"
    msg += "/listing + username - List your repositories \n"
    msg += "/info + username - shows your information \n"
    msg += "Ex: /listing HeavenH | /info HeavenH"

    # Send the message
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg.format(
                         user_name=update.message.from_user.first_name,
                         bot_name=bot.name))


# Function to list the repositories
def listing(bot, update, args):
    gh = GitHub()
    for user in args:
        bot.send_message(chat_id=update.message.chat_id,
                         text='{0} Listing the user repositories '
                         .format('\U0001F5C4') +
                         '[{0}](https://github.com/{0}) {1}'.format(
                             user, Emoji.WHITE_DOWN_POINTING_BACKHAND_INDEX),
                         parse_mode=ParseMode.MARKDOWN)

        bot.send_message(chat_id=update.message.chat_id,
                         text=gh.get_repos(user))


# Function to display user information
def info(bot, update, args):
    gh = GitHub()
    for user in args:
        bot.send_message(chat_id=update.message.chat_id,
                         text='{2} User Information ' +
                         '[{0}](https://github.com/{0}) {1}'.format(
                             user, Emoji.WHITE_DOWN_POINTING_BACKHAND_INDEX,
                             Emoji.INFORMATION_SOURCE),
                         parse_mode=ParseMode.MARKDOWN)
        bot.send_message(chat_id=update.message.chat_id,
                         text=gh.get_info(user))

# Add handlers to dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('listing', listing, pass_args=True))
dispatcher.add_handler(CommandHandler('info', info, pass_args=True))

# Start the program
up.start_polling()

# Developed by Heaven, Jr750ac, Pedro Souza, Israel Sant'Anna all rights
# reserved
