def riffle(n):    
    cardList = list(range(0,n))
    shuffledList = []
    middleIndex = len(cardList) // 2
    index = 0
    while (shuffledList != cardList):
        tmpList = []
        if index == 0:
            shuffledList = cardList
            
        firsthalf = shuffledList[:middleIndex]
        secondhalf = shuffledList[middleIndex:]
        for i in range(0,middleIndex):
            tmpList += [firsthalf[i]]
            tmpList += [secondhalf[i]]
            
        shuffledList = tmpList
        index += 1
    return index

print(riffle(52))