from IRC_bot import *
from workers import *
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


################ Print Chat Connection Info ################
text = ""
while text.find(f"JOIN {channel}") < 0:
    text = irc.get_response()
    print(text + "\n")
################ Print Chat Connection Info ################



################ WORKER INITIALIZATION ################
messageCache = [] # Initialize the autotracking message queue
cleaner = messageQueueCleaner(1, messageCache)
talkerList = [] # Initialize talker list
tracker = userTracker(2, messageCache, talkerList)
################ WORKER INITIALIZATION ################


################ MAIN PROCESS EXECUTION ################
while True:
    text = irc.get_response()
    print(text)
    if checkSwear(BANNED_WORDS, text):
        irc.send(channel, "OOPS")

        #store cache
    cacheItem = [time.process_time(), text.rstrip()]
    messageCache.append(cacheItem)
################ MAIN PROCESS EXECUTION ################
