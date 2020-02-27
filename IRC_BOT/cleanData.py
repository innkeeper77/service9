
def readData(dataList):
    with open('BANNABLE_WORDS') as f:
        for line in f:
            if line.lower() not in dataList:
                dataList.append(line.lower())

def writeData(dataList):
    with open('BANNED_WORDS','w') as f:
        for word in dataList:
            f.write(word)

entries = []

readData(dataList=entries)
entries.sort()

leet = []
replacements = ( ('a','4'), ('b','8'), ('c','('), ('e','3'), ('g','9'),
                 ('h','#'), ('l','1'), ('o','0'), ('t','+'), ('s','5'),
                 ('t','7'), ('z','2') )
for word in entries:
    new_word = word
    leet.append(new_word)
    for old, new in replacements:
        new_word = new_word.replace(old, new)
        if new_word not in leet:
            leet.append(new_word)


# for index,word in enumerate(entries):
#     print(word + " " + leet[index])
#
# for word in entries:
#     print(word)
#
# leet.sort()
#
# for word in leet:
#     if word not in entries:
#         entries.append(word.lower())

# for word in entries:
    # print(word)
writeData(dataList=leet)
# writeData(dataList=leet)
