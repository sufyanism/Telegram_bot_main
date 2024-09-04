from telegram import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup # type: ignore
from telegram.ext import Updater, MessageHandler, CommandHandler, CallbackQueryHandler, ConversationHandler ,Filters # type: ignore
import requests # type: ignore
import os

PORT = os.environ.get("TELEGRAM_ID")

FIRST,SONGS, HELP= range(3)

def start(bot, update):
    print("START")
    keyboard = [
        [
            KeyboardButton("About"), KeyboardButton("Songs")    ],
        [   KeyboardButton("Social Media"), KeyboardButton("Cancel")  ],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    bot.message.reply_text(
        u"Select any of the following buttons given below",
        reply_markup=reply_markup
    ) 
    return FIRST

def one(bot, update):

# About Button
    if  bot.message.text == 'About':
        print("ABOUT")
        bot.message.reply_text('He is punjabi singer')

# Cancel Button
    elif bot.message.text == 'Cancel':
        print("CANCEL")
        bot.message.reply_text("End conversation, You can type \ /start to run this bot")
        return ConversationHandler.END

# Instagram Button

    elif bot.message.text == 'Instagram':
        bot.message.reply_text("https://www.instagram.com/navaansandhu")
    
# Youtube Button
    elif bot.message.text == 'Youtube':
        bot.message.reply_text("https://www.youtube.com/c/NavaanSandhuOfficial")

# Social Media Button
    elif bot.message.text == 'Social Media':
        print("Media")
        keyboard = [
        [
           KeyboardButton("Instagram"),KeyboardButton("Youtube")],
           [ KeyboardButton("Options")  ],
    ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        bot.message.reply_text(
        u"Select any of the following buttons given below",
        reply_markup=reply_markup
    )  
        return FIRST


 

# Songs Button
    elif bot.message.text == 'Songs' :
        print("SONGS")
        keyboard = [
            [   InlineKeyboardButton("Jealousy", callback_data='Jealousy'),
                InlineKeyboardButton("Black Life", callback_data='Black Life')
            ],
           [    InlineKeyboardButton("Radio", callback_data='Radio'),
                InlineKeyboardButton("Asle", callback_data='Asle')
            ],
            [                
            InlineKeyboardButton("Back", callback_data='Back')
            ]
              ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.message.reply_text('Please choose:', reply_markup=reply_markup)
        return SONGS


# Help Button
    elif bot.message.text == 'Help':
        print("HELP")
        bot.message.reply_text("""
        Contact admin for help
        """)

# Options Button

    elif bot.message.text == 'Options':
        print("OPTIONS")
        keyboard = [
        [
            KeyboardButton("About"), KeyboardButton("Songs")    ],
        [   KeyboardButton("Social Media"), KeyboardButton("Cancel")  ],
    ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        bot.message.reply_text(
        u"Select any of the following buttons given below",
        reply_markup=reply_markup
    )

    else:
        keyboard = [
          [
        KeyboardButton("Help"),
        KeyboardButton("Options"),
        ],
    ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        bot.message.reply_text(
        u"Get help",
        reply_markup=reply_markup
    ) 
        return FIRST

# Songs Method
def songs(bot, update):
    print("SONGS", bot)
    """Parses the CallbackQuery and updates the message text."""
    query = bot.callback_query
    query.answer()

# Button 1
    if query.data  == 'Jealousy':
       query.message.reply_text("https://www.youtube.com/watch?v=wXLFrdUlp-A : {query.data}")
       return FIRST

# Button 2
    if query.data  == 'Black Life':
        query.message.reply_text("https://www.youtube.com/watch?v=vTclN-xmX4E : {query.data}")
        return FIRST

# Button 3
    if query.data  == 'Radio':
        query.message.reply_text("https://www.youtube.com/watch?v=RlIiOIqPLBU : {query.data}")
        return FIRST

# Button 4
    if query.data  == 'Asle':
        query.message.reply_text("https://www.youtube.com/watch?v=9Wb2GIToZfg : {query.data}")
        return FIRST

# Button 5
    if query.data == 'Back':
        query.message.reply_text("Back to main menu")
        return FIRST
    
# Main method
def main():
    updater = Updater("5147821908:AAEcjnbgFXtUfI41AADsYag8-7j8HKyM5KI")
    print(updater)
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST:[MessageHandler(Filters.text, callback=one)],
            SONGS :[CallbackQueryHandler(callback=songs)],
            },
        fallbacks=[CommandHandler('start', start)]
            )

    APIKEY = "ADD_YOUR_TELEGRAM_API_KEY"

    updater.dispatcher.add_handler(conv_handler)
    updater.start_webhook(listen="0.0.0.0",port= os.environ.get("PORT",443), url_path= APIKEY, webhook_url="https://jk-telegram-bot.herokuapp.com/" + APIKEY)
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()