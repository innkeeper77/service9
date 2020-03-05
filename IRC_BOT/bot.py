from IRC_bot import *
from workers import *
from functions import *
import re
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


################ Print Chat Connection Info ################
text = ""
while text.find(f"JOIN {channel}") < 0:
    text = irc.get_response()
    print(text + "\n")
################ Print Chat Connection Info ################



################ WORKER INITIALIZATION ################
messageCache = [] # Initialize the autotracking message queue
cleaner = messageQueueCleaner(1, messageCache)
talkerDict = {} # Initialize talker dictionary
tracker = userTracker(2, messageCache, talkerDict)
################ WORKER INITIALIZATION ################

BANNED_WORDS = readData()

################ MAIN PROCESS EXECUTION ################
while True:
    text = irc.get_response()
    print(text)

    """ Check for swearing """
    if checkSwear(BANNED_WORDS, text):
            #extract username
        badUser = re.findall(r'(?<=\:)(.*?)(?=\!)',text)
        if len(badUser) > 0:
            irc.send(channel, f"clean it up @{badUser[0]}!")

    """ Check for spam """
    if checkSpam(talkerDict):
        badUser = re.findall(r'(?<=\:)(.*?)(?=\!)',text)
        if len(badUser) > 0:
            irc.send(channel, f"Settle Down @{badUser[0]}!")

        #store cache
    cacheItem = [time.process_time(), text.rstrip()]
    messageCache.append(cacheItem)
################ MAIN PROCESS EXECUTION ################
