import threading
import time
import re

class messageQueueCleaner(object):
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
            print(f"Cleaning the queue of size {len(self.queue)} in background.")
                #if the oldest message is out of range, delete it
            while(len(self.queue) > 0 and time.process_time() - self.queue[0][0] > 0.01):
                self.queue.pop(0)

            time.sleep(self.interval)

class userTracker(object):
    """ userTracker constructs a list of users that are talking in real time """
    def __init__(self, interval, queue, usernameDict):
        """ constructor function """
        self.interval = interval
        self.queue = queue
        self.usernameDict = usernameDict
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        """ Process to run at specified intervals """
        while True:
            print("Updating talker list usernames.")
            self.usernameDict.clear()
            if len(self.queue) > 0:
                for talker in self.queue:
                    if(len(re.findall(r'(?<=\:)(.*?)(?=\!)', talker[1])) > 0):
                        user_name = re.findall(r'(?<=\:)(.*?)(?=\!)', talker[1])[0]
                        if user_name in self.usernameDict:
                                #extract the username from all messages in queue and store
                            self.usernameDict[user_name] += 1;
                        else:
                                #extract the username from all messages in queue and store
                            self.usernameDict[user_name] = int(1);

            print(self.usernameDict)
            time.sleep(self.interval)
