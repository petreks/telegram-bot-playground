# https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot2.py

from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
from telegram.ext.dispatcher import run_async

def start(update, context):
    update.message.reply_text('How can I help, your Majesty?')

def chat(update, context):
    print("Generating reply message...")
    incoming_text = update.message.text.lower()
    reply_text = get_reply(incoming_text)
    update.message.reply_text(reply_text)

def get_reply(incoming_text):
    print("Got the message: " + incoming_text)
    if incoming_text == "mirror, mirror on the wall, who's the fairest of them all?":
        return "Thou, O Queen, art the fairest in the land"
    elif ("mirror" in incoming_text) or ("mirror on the wall" in incoming_text):
        return "Yes?"
    elif "who’s the fairest of them all" in incoming_text:
        return "Snow White, O Queen, is the fairest of them all"
    else:
        return "I know nothing, I'm Jon Snow..."

def main():
    updater = Updater('REPLACE_WITH_YOUR_TOKEN', use_context=True)
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, chat))
    
    updater.start_polling()
    print("Start polling...")
    updater.idle()

if __name__ == '__main__':
    print("Starting the program...")
    main()
