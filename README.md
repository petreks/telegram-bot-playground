# telegram-bot-playground
Trying out some telegram Bot tutorials.

# Useful Resources
Official Docs:
- https://core.telegram.org/bots/samples
- https://github.com/python-telegram-bot/python-telegram-bot
- https://github.com/eternnoir/pyTelegramBotAPI

Online Tutorial:
- https://www.freecodecamp.org/news/learn-to-build-your-first-bot-in-telegram-with-python-4c99526765e4/

Hosting Bot:
- https://github.com/python-telegram-bot/python-telegram-bot/wiki/Hosting-your-bot
- https://github.com/python-telegram-bot/python-telegram-bot/wiki/Where-to-host-Telegram-Bots

Possible Bot ideas - APIs:
- https://data.gov.sg/dataset/realtime-weather-readings
- https://github.com/ml5js/ml5-examples/tree/master
- https://deepai.org/apis
- https://deepai.org/machine-learning-model/fast-style-transfer

# Basic Steps
1. Set up
  - Install Python: https://www.python.org/downloads/
  - Install Python Libraries
  ```
  pip3 install python-telegram-bot
  pip3 install requests
  ```
2. Register Bot: https://core.telegram.org/bots#6-botfather
3. Run the python Program - your Bot will be online
  ```
  python dog_pic_gen.py
  ```
  
# Examples
1. random dog picture generator. followed [tutorial](https://www.freecodecamp.org/news/learn-to-build-your-first-bot-in-telegram-with-python-4c99526765e4/)
- <img src="https://github.com/qiyun28/telegram-bot-playground/blob/master/dog_pic_gen.png" width=400>

2. chat bot. followed official [example](https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot2.py)
- <img src="https://github.com/qiyun28/telegram-bot-playground/blob/master/chat_bot.png" width=400>

3. image style transfer. using deep AI [API](https://deepai.org/machine-learning-model/fast-style-transfer)
- content picture (Photo by Igor Stepanov on Unsplash)
- <img src="https://github.com/qiyun28/telegram-bot-playground/blob/master/igor-stepanov-5uUPrmZgEYM-unsplash.jpg" width=350>
- style picture
- <img src="https://github.com/qiyun28/telegram-bot-playground/blob/master/europeana-uS5LXujNOq4-unsplash.jpg" width=350>
- <img src="https://api.deepai.org/job-view-file/06e4f9d5-ae20-493e-9d6d-5524056e4570/outputs/output.png" width=350>
