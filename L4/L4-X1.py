import time

wordlist = open('ordlistau.txt', encoding='utf8').read().split()

def linsearch(list, element):
    return element in list

def binsearch(list, element):    
    lowIndex = 0
    hiIndex = len(list) - 1
    while lowIndex <= hiIndex:
        middle = (lowIndex+hiIndex) // 2
        if element < list[middle]:
            hiIndex = middle -1
        elif element > list[middle]:
            lowIndex = middle + 1
        else:
            return True
    return False

def searchPair(list, function):
    pairWordList = []
    for word in list:
        pairWord = word[2:5] + word[0:2]
        if function(list, pairWord):
            pairWordList += [(word, pairWord)]
    return pairWordList

#print(searchPair(wordlist, linsearch))
#print(searchPair(wordlist, binsearch))
         