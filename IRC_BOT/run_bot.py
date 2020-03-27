""" This holds the main operational functions of the bot. """
import re
import time
import threading
from collections import namedtuple

import irc
import workers
import functions as func

BotConfigurations = namedtuple("BotConfigurations", ["name",
                                                     "server",
                                                     "channel",
                                                     "interval",
                                                     "message_limit"])

def run_bot(config, lock):
    """ main bot function, check for swears and spam """
    #################### IRC CONFIG ####################
    port = 6666
    botnick = config.name
    #################### IRC CONFIG ####################


    ################ IRC INITIALIZATION ################
    IRC = irc.IRC()
    IRC.connect(config.server, port, config.channel, botnick)
    IRC.send(config.channel, f"{botnick} logging on")
    ################ IRC INITIALIZATION ################


    ################ Print Chat Connection Info ################
    response = ""
    while response.find(f"JOIN {config.channel}") < 0:
        response = IRC.get_response().rstrip()
        with lock:
            print('{}: {}\n'.format(botnick, response))
    ################ Print Chat Connection Info ################



    ################ WORKER INITIALIZATION ################
    message_cache = [] # Initialize the autotracking message queue
    cleaner = workers.MessageQueueCleaner(config.interval, message_cache)
    talker_dict = {} # Initialize talker dictionary
    tracker = workers.UserTracker(config.interval, message_cache, talker_dict)
    ################ WORKER INITIALIZATION ################

    banned_words = func.read_data("BANNED_WORDS")

    ################ MAIN PROCESS EXECUTION ################
    while True:
        response = IRC.get_response().rstrip()
        with lock:
            print('{}: {}'.format(botnick, response))

        # Check for swearing
        if func.test_match(banned_words, response):
            bad_user = re.findall(r'(?<=\:)(.*?)(?=\!)', response) #extract username
            if len(bad_user) > 0:
                IRC.send(config.channel, f"Clean it up @{bad_user[0]}!")

        # Check for spam
        if func.test_max(talker_dict, config.message_limit):
            bad_user = re.findall(r'(?<=\:)(.*?)(?=\!)', response) #extract username
            talker_dict[bad_user] = 0
            if len(bad_user) > 0:
                IRC.send(config.channel, f"Take about 20% off there @{bad_user[0]}!")

        #store message in cache
        message_cache.append([time.process_time(), response.rstrip()])
    ################ MAIN PROCESS EXECUTION ################

if __name__ == '__main__':
    TEST = BotConfigurations("foobot", "chat.freenode.net", "#kaestChannels", 0.1, 3)
    LOCK = threading.Lock()
    run_bot(config=TEST, lock=LOCK)
