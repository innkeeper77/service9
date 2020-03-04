from IRC_bot import *
from functions import *
import time

#################### IRC CONFIG ####################
port = 6666
server = "chat.freenode.net"
channel = "#kaestChannels"
botnick = "FooBot"
botnickpass = "apassword"
botpass = "<%= @apassword_password %>"
#################### IRC CONFIG ####################



################ IRC INITIALIZATION ################
irc = IRC()
irc.connect(server, port, channel, botnick, botpass)
irc.send(channel, f"{botnick} logging on")
################ IRC INITIALIZATION ################


BANNED_WORDS = readData()
BOOT = False
listen = False


while True:
    text = irc.get_response()
    print(text)

    if checkSwear(BANNED_WORDS,text):
        irc.send(channel, "OOPS")
