from datetime import datetime

import secret
import schedule
import telebot
import time

bot = telebot.TeleBot(secret.get_token())


def send_message():
    if get_trash_cleaner_name(get_week_day()) != "error":
        bot.send_message(secret.get_group_id(), get_message(get_week_day()))


def get_message(week_day):
    message = 'Сегодня ' + \
              week_day + '-й день, ' + \
              get_trash_cleaner_name(week_day) + \
              ' вынеси мусор \n ' + \
              secret.get_mention(get_trash_cleaner_name(week_day))
    return message


def get_week_day():
    return str(datetime.isoweekday(datetime.today()))


def get_trash_cleaner_name(week_day):
    return {
        '1': 'Ваня',
        '2': 'Артур Б',
        '3': 'Влад',
        '5': 'Рол',
        '6': 'Слава',
    }.get(week_day, 'error')


def main():
    schedule.every().day.at("20:00").do(send_message)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
