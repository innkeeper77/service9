from IRC_bot import *



def readData():
    dataList = []
    with open('BANNED_WORDS') as f:
        for line in f:
            if line.lower() not in dataList:
                dataList.append(line.rstrip().lower())
    return dataList


## IRC Config
BANNED_WORDS = readData()
server = "chat.freenode.net"
port = 6666
channel = "#kaestchnnel"
botnick = "CHARLIE1995"
botnickpass = "yourpassword"
botpass = "<%= @yourpassword_password %>"
irc = IRC()
irc.connect(server, port, channel, botnick, botpass)
irc.send(channel, "Hello World")

while True:
    text = irc.get_response()
    print(text)

    for word in BANNED_WORDS:
        if word in text:
            irc.send(channel, "Your language is a royal blue. I'm going to need you to take it down to a powder blue.")
            break
