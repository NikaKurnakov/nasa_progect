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
        bot.send_photo(chat_id, open(f"images/{args.file}", 'rb'))
    else:
        bot.send_photo(chat_id, open(random.choice(files), 'rb'))


def main():
    load_dotenv()
    token_bot = os.environ['TOKEN_BOT']
    chat_id = os.environ['CHAT_ID']
    files = glob.glob("images/*.png")
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="интересующий файл")
    args = parser.parse_args()
    send_photo(token_bot, args, chat_id, files)


if __name__ == '__main__':
    main()