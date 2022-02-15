import config
import telebot
import schedule, time

bot = telebot.TeleBot(config.token)


# def send_message():
#     bot.send_message(-508454043, "хм че не отправляет")


def main():
    # schedule.every().day.at("21:17").do(send_message)
    bot.send_message(-508454043, "хм че не отправляет")
    # send_message()
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)


if __name__ == '__main__':
    main()
