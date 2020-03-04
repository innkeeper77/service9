def readData():
    dataList = []
    with open('BANNED_WORDS') as f:
        for line in f:
            if line.lower() not in dataList:
                dataList.append(line.rstrip().lower())
    return dataList

def checkSwear(list, text):
    for word in list:
        if word in text:
            return True
    return False
