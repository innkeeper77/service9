
def readData():
    dataList = []
    with open('BANNED_WORDS') as f:
        for line in f:
            if line.lower() not in dataList:
                dataList.append(line.rstrip().lower())
    return dataList

def checkSwear(list, text):
    for word in list:
        if text.find(word) > 0:
            return True
    return False

def checkSpam(users):
    for user in users:
        if users[user] > 5:
            return True
    return False
