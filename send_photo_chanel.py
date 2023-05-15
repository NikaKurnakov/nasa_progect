import random
import glob
import time
import os
import telegram
from dotenv import load_dotenv
import argparse


def send_photo_tg_chanel(delay_time, token_bot, files, chat_id):
    bot = telegram.Bot(token=token_bot)
    for file in files:
        with open(file, 'rb'):
            bot.send_photo(chat_id)
            time.sleep(int(delay_time))


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("--delay", help="время задержки в секундах")
    args = parser.parse_args()
    delay_time = os.environ['DELAY']
    if args.delay:
        delay_time = args.delay
    token_bot = os.environ['TG_TOKEN_BOT']
    chat_id = os.environ['CHANEL_CHAT_ID']
    files = glob.glob("images/*.png")
    while True:
        send_photo_tg_chanel(delay_time, token_bot, files, chat_id)
        files = random.shuffle(files)


if __name__ == '__main__':
    main()
