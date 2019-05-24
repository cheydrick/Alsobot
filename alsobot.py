import random
import os
import sys

from matrix_bot_api.matrix_bot_api import MatrixBotAPI
from matrix_bot_api.mregex_handler import MRegexHandler
from matrix_bot_api.mcommand_handler import MCommandHandler
from mcstatus import MinecraftServer

class Alsobot(object):
    def __init__(self, minecraftserver):
        self.minecraftserver = minecraftserver
        self.minecraftserver_handle = MinecraftServer(self.minecraftserver)

    def default_response(self, room, event):
        status = self.minecraftserver_handle.status()
        if status.players.online == 0:
            info_string = "The server has 0 players and replied in {1}ms"
        else:
            info_string = "The Server has {0} players and replied in {1}ms:\n".format(status.players.online, status.latency)
            for p in range(status.players.online):
                info_string += "{}\n".format(status.players.sample[p].name)
        
        room.send_text(info_string)

def alsobot_test_callback(room, event):
    server = MinecraftServer(MINECRAFTSERVERNAME)
    status = server.status()
    info_string = "The server has {0} players and replied in {1} ms".format(status.players.online, status.latency)
    room.send_text(info_string)

if __name__ == '__main__':
    USERNAME = os.getenv('ALSOBOTUSER', "")
    PASSWORD = os.getenv('ALSOBOTPASSWORD', "")
    SERVER = os.getenv('ALSOBOTSERVER', "")
    MINECRAFTSERVER = os.getenv('ALSOBOTMINECRAFTSERVER', "")
    if (USERNAME or PASSWORD or SERVER or ALSOBOTMINECRAFTSERVER) == "":
        #print("{} {} {}".format(USERNAME, PASSWORD, SERVER))
        print("Set ALSOBOTUSER, ALSOBOTPASSWORD, ALSOBOTSERVER, or ALSOBOTMINECRAFTSERVER environment variables!")
        sys.exit()

    matrix_bot = MatrixBotAPI(USERNAME, PASSWORD, SERVER)
    alsobot = Alsobot(MINECRAFTSERVER)
    alsobot_test_handler = MRegexHandler("alsobot", alsobot.default_response)
    matrix_bot.add_handler(alsobot_test_handler)
    matrix_bot.start_polling()

    while True:
        input()
