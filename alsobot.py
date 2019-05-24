import random
import os
import sys

from matrix_bot_api.matrix_bot_api import MatrixBotAPI
from matrix_bot_api.mregex_handler import MRegexHandler
from matrix_bot_api.mcommand_handler import MCommandHandler

def alsobot_test_callback(room, event):
    room.send_text("Hi, " + event['sender'])

if __name__ == '__main__':
    USERNAME = os.getenv('ALSOBOTUSER', "")
    PASSWORD = os.getenv('ALSOBOTPASSWORD', "")
    SERVER = os.getenv('ALSOBOTSERVER', "")

    if (USERNAME or PASSWORD or SERVER) == "":
        print("{} {} {}".format(USERNAME, PASSWORD, SERVER))
        print("Set ALSOBOTUSER, ALSOBOTPASSWORD, and ALSOBOTSERVER environment variables!")
        sys.exit()

    alsobot = MatrixBotAPI(USERNAME, PASSWORD, SERVER)
    alsobot_test_handler = MRegexHandler("alsobot", alsobot_test_callback)
    alsobot.add_handler(alsobot_test_handler)
    alsobot.start_polling()

    while True:
        input()
