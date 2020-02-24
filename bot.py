from IRC_bot import *

## IRC Config
server = "chat.freenode.net"
port = 6666
channel = "#YOURCHANNEL"
botnick = "YOURBOTNAME"
botnickpass = "yourpassword"
botpass = "<%= @yourpassword_password %>"
irc = IRC()
irc.connect(server, port, channel, botnick, botpass)
irc.send(channel, "Hello World")

while True:
    text = irc.get_response()
    print(text)
