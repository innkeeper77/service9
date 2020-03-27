""" Trystan Kaes
    IRC bot
    March 4, 2020 """
import threading

import run_bot as rb


SERVER = "chat.freenode.net"
CHANNELS = ["#kaestChannels", "#kaestOtherChannels", "#andOneMoreKaest"]


if __name__ == '__main__':
    LOCK = threading.Lock()

    for i, CHANNEL in enumerate(CHANNELS):
        CONFIG = rb.BotConfigurations("foobot"+str(i), SERVER, CHANNEL, 0.1, 2)

        thread = threading.Thread(target=rb.run_bot, args=(CONFIG, LOCK))
        thread.start()
