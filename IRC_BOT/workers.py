import threading
import re as regex
import time

class messageQueueCleaner(object):
    def __init__(self, interval, queue):
        self.interval = interval
        self.queue = queue
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            print(f"Cleaning the queue of size {len(self.queue)} in background.")
            while(len(self.queue) > 0 and time.process_time() - self.queue[0][0] > 0.01):
                self.queue.pop(0)

            time.sleep(self.interval)

class userTracker(object):
    def __init__(self, interval, queue, usernameList):
        self.interval = interval
        self.queue = queue
        self.usernameList = usernameList
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            print("Updating talker list usernames.")
            if len(self.queue) > 0:
                self.usernameList.clear()
                for talker in self.queue:
                    self.usernameList.append(regex.findall(r'(?<=\:)(.*?)(?=\!)', talker[1]))
                # print(self.usernameList)
            time.sleep(self.interval)
