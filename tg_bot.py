import telegram
import os
from dotenv import load_dotenv
import argparse
import random
import glob


def send_photo(token_bot, args, chat_id, files):
    bot = telegram.Bot(token=token_bot)
    bot.send_message(text='Привет!', chat_id=chat_id)
    if args.file:
        with open(os.path.join("images", args.file), 'rb'):
            bot.send_photo(chat_id)
    else:
        with open(random.choice(files), 'rb'):
            bot.send_photo(chat_id)


def main():
    load_dotenv()
    token_bot = os.environ['TG_TOKEN_BOT']
    chat_id = os.environ['TG_CHANEL_CHAT_ID']
    files = glob.glob("images/*.png")
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="интересующий файл")
    args = parser.parse_args()
    send_photo(token_bot, args, chat_id, files)


if __name__ == '__main__':
    main()
