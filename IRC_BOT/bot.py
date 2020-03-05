""" Trystan Kaes
    IRC bot
    March 4, 2020 """
import re
import time
import irc
import workers
import functions as func


#################### IRC CONFIG ####################
PORT = 6666
SERVER = "chat.freenode.net"
CHANNEL = "#kaestChannels"
BOTNICK = "FooBot"
#################### IRC CONFIG ####################


################ IRC INITIALIZATION ################
IRC = irc.IRC()
IRC.connect(SERVER, PORT, CHANNEL, BOTNICK)
IRC.send(CHANNEL, f"{BOTNICK} logging on")
################ IRC INITIALIZATION ################


################ Print Chat Connection Info ################
RESPONSE = ""
while RESPONSE.find(f"JOIN {CHANNEL}") < 0:
    RESPONSE = IRC.get_response()
    print(RESPONSE + "\n")
################ Print Chat Connection Info ################



################ WORKER INITIALIZATION ################
MESSAGE_CACHE = [] # Initialize the autotracking message queue
CLEANER = workers.MessageQueueCleaner(1, MESSAGE_CACHE)
TALKER_DICT = {} # Initialize talker dictionary
TRACKER = workers.UserTracker(2, MESSAGE_CACHE, TALKER_DICT)
################ WORKER INITIALIZATION ################

BANNED_WORDS = func.read_data("BANNED_WORDS")

################ MAIN PROCESS EXECUTION ################
while True:
    RESPONSE = IRC.get_response()
    print(RESPONSE)

    # Check for swearing
    if func.test_match(BANNED_WORDS, RESPONSE):
        BAD_USER = re.findall(r'(?<=\:)(.*?)(?=\!)', RESPONSE) #extract username
        if len(BAD_USER) > 0:
            IRC.send(CHANNEL, f"clean it up @{BAD_USER[0]}!")

    # Check for spam
    if func.test_max(TALKER_DICT, 5):
        BAD_USER = re.findall(r'(?<=\:)(.*?)(?=\!)', RESPONSE) #extract username
        if len(BAD_USER) > 0:
            IRC.send(CHANNEL, f"Settle Down @{BAD_USER[0]}!")

        #store message in cache
    MESSAGE_CACHE.append([time.process_time(), RESPONSE.rstrip()])
################ MAIN PROCESS EXECUTION ################
