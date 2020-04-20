# using deep ai apis
# https://deepai.org/machine-learning-model/fast-style-transfer

from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.ext.dispatcher import run_async
import requests
import re

def image_tranfer():
    r = requests.post(
        "https://api.deepai.org/api/fast-style-transfer",
        data={
            'content': 'https://www.mantruckandbus.com/fileadmin/media/bilder/02_19/219_05_busbusiness_interviewHeader_1485x1254.jpg',
            'style': 'https://assets.vogue.com/photos/5be9ddde6bcde32d2941381e/master/w_1280%2Cc_limit/Picasso%2C%252520La%252520Lampe.jpg',
        },
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    print(r.json())
    return r.json().get('output_url')


@run_async
def transfer(update, context):
    print("Getting picture...")
    url = image_tranfer()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('REPLACE_WITH_YOUR_TOKEN', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('transfer',transfer))
    # dp.add_handler(CommandHandler(MessageHandler(Filters.photo, )))
    updater.start_polling()
    print("Start polling...")
    updater.idle()

if __name__ == '__main__':
    print("Starting the program...")
    main()
