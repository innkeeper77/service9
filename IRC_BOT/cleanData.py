
def readData(dataList):
    with open('BANNABLE_WORDS') as f:
        for line in f:
            if line.lower() not in dataList:
                dataList.append(line.lower())

###############################################

def writeData(dataList, filename):
    with open(filename,'w') as f:
        for word in dataList:
            f.write(word)



###############################################
replacements = ( ('a','4'), ('b','8'), ('c','('), ('e','3'), ('g','9'),
                 ('h','#'), ('l','1'), ('o','0'), ('t','+'), ('s','5'),
                 ('t','7'), ('z','2') )
entries = []
leet = []

#read in data
readData(dataList=entries)

#sort
entries.sort()

#update the main file without duplicates in alphabetical order
writeData(dataList=entries, filename="BANNABLE_WORDS")


#generate all the leetspeach phrases
for word in entries:
    new_word = word
    leet.append(new_word)
    for old, new in replacements:
        new_word = new_word.replace(old, new)
        if new_word not in leet:
            leet.append(new_word)


#update the actual banned list
writeData(dataList=leet, filename="BANNED_WORDS")
