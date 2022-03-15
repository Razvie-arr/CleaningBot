import config
import telebot
import schedule, time
from datetime import datetime

bot = telebot.TeleBot(config.token)


def send_message():
    bot.send_message(-508454043, get_message(get_week_day()))


def get_message(week_day):
    message = 'Сегодня ' + week_day + '-й день, ' + get_trash_cleaner_name(week_day) + ' вынеси мусор, ' + get_mention(get_trash_cleaner_name(week_day))
    return message


def get_week_day():
    return str(datetime.isoweekday(datetime.today()))


def get_trash_cleaner_name(week_day):
    return {
        '1': 'Ваня',
        '2': 'Артур Б',
        '3': 'Влад',
        '4': 'Артур О',
        '5': 'Рол',
        '6': 'Сеня',
        '7': 'Артур М'
    }.get(week_day, 'error')


def get_mention(trash_cleaner_name):
    return {
        'Ваня': '@Falx1',
        'Артур Б': '@pretty_snyder',
        'Влад': '@Razviearr',
        'Артур О': '@hovhannesyan',
        'Рол': '@arakelian',
        'Сеня': '',
        'Артур М': '@everyonehatesarthur'
    }.get(trash_cleaner_name, 'error')


def main():
    schedule.every().day.at("18:00").do(send_message)
    schedule.every().day.at("20:00").do(send_message)
    schedule.every().day.at("21:00").do(send_message)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
