""" Contains class definitions for all multithreaded workers. """
import threading
import time
import re

class MessageQueueCleaner():
    """ messageQueueCleaner updates the message queue to only hold a specified time range """
    def __init__(self, interval, queue):
        """ constructor function """
        self.interval = interval
        self.queue = queue
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        """ Process to run at specified intervals """
        while True:
            # print(f"Cleaning the queue of size {len(self.queue)} in background.")
                #if the oldest message is out of range, delete it
            while(len(self.queue) > 0 and time.process_time() - self.queue[0][0] > 0.01):
                self.queue.pop(0)

            time.sleep(self.interval)

class UserTracker():
    """ userTracker constructs a list of users that are talking in real time """
    def __init__(self, interval, queue, username_dict):
        """ constructor function """
        self.interval = interval
        self.queue = queue
        self.username_dict = username_dict
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        """ Process to run at specified intervals """
        while True:
            # print("Updating talker list usernames.")
            self.username_dict.clear()
            if len(self.queue) > 0:
                #count how many messages have been sent per user in queue
                for talker in self.queue:
                    if len(re.findall(r'(?<=\:)(.*?)(?=\!)', talker[1])) > 0:
                        user_name = re.findall(r'(?<=\:)(.*?)(?=\!)', talker[1])[0]
                        if user_name in self.username_dict:
                                #extract the username from all messages in queue and store
                            self.username_dict[user_name] += 1
                        else:
                                #extract the username from all messages in queue and store
                            self.username_dict[user_name] = int(1)
            time.sleep(self.interval)
