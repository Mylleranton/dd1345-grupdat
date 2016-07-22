import time

wordlist = open('ordlistau.txt', encoding='utf8').read().split()

def linsearch(list, element):
    return element in list

def linsearchPair(list):
    pairWordList = []
    for word in list:
        pairWord = word[2:5] + word[0:2]
        if linsearch(list, pairWord):
            pairWordList += [(word, pairWord)]
    return pairWordList

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

def binsearchPair(list):
    pairWordList = []
    for word in list:
        pairWord = word[2:5] + word[0:2]
        if binsearch(list, pairWord):
            pairWordList += [(word, pairWord)]
    return pairWordList

def linsearchTest():
    while True:
        userWord = input('Ditt ord: ')
        if linsearch(wordlist, userWord):
            print(userWord + ' finns.')
        else:
            print(userWord + ' finns ej.')

def binsearchTest():
    while True:
        userWord = input('Ditt ord: ')
        if binsearch(wordlist, userWord):
            print(userWord + ' finns.')
        else:
            print(userWord + ' finns ej.')
         
def linsearchPairTest():
    print(linsearchPair(wordlist))

def binsearchPairTest():
    print(binsearchPair(wordlist))

binsearchPairTest()