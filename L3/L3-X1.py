# -*- coding: utf-8 -*-
vowels = 'aouåeiyäöAOUÅEIYÄÖ'
consonants = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'

def visk(instring):
    outstring = ''
    for i in instring:
        if i not in vowels:
            outstring += i
    return outstring

def rovar(instring):
    outstring = ''
    for i in instring:
        if i in consonants:
            outstring += i + 'o' + i
        elif i in vowels:
            outstring += i
        else:
            outstring += i
    return outstring

def fylle(instring):
    outstring = ''
    for i in instring:
        if i in consonants:
            outstring += i
        elif i in vowels:
            outstring += i + 'f' + i
        else:
            outstring += i
    return outstring

def bebis(instring):
    instringList = instring.split()
    outstringList = []
    for word in instringList:
        outword = ''
        for i in word:
            if i in consonants:
                outword += i
            elif i in vowels:
                outword += i
                outword *= 3
                outstringList += [outword]
                break
    outstring = ' '.join(outstringList)
    return outstring
    
def alla(instring):
    instringList = instring.split()
    outstringList = []
    for word in instringList:
        charsbeforevowel = ''
        foundbreakpoint = False
        outword = ''
        for i in word:
            if foundbreakpoint == True: 
                outword += i
            elif i in consonants:
                charsbeforevowel += i
            elif i in vowels:
                outword += i
                foundbreakpoint = True
                    
        outstringList += [outword + charsbeforevowel + 'all']    
    outstring = ' '.join(outstringList)
    return outstring
    
def fikon(instring):
    instringList = instring.split()
    outstringList = []
    for word in instringList:
        charsbeforebreak = ''
        foundbreakpoint = False
        outword = ''
        for i in word:
            if foundbreakpoint == True: 
                outword += i
            elif i in consonants:
                charsbeforebreak += i
            elif i in vowels:
                charsbeforebreak += i
                foundbreakpoint = True
                    
        outstringList += ['fi' + outword + charsbeforebreak + 'kon']    
    outstring = ' '.join(outstringList)
    return outstring
    
functions = [visk,rovar,fylle,bebis,alla,fikon]
functionsName = ['Viskarspråket', 'Rövarspråket', 'Fyllespråket', 'Bebisspråket', 'Allspråket', 'Fikonspråket', 'Avsluta programmet']

while True:
    print('Vilket språk önskas?')
    index = 1
    for string in functionsName:
        print(str(index) + ' ' + string)
        index += 1
    choice = int(input(''))
    
    if choice > index:
        break
    elif choice == index - 1:
        print('Hej då!')
        break
    
    inputSentence = raw_input('Din mening: ')
    translatedSentence = functions[choice-1](inputSentence)
    print(functionsName[choice-1] + ': ' + translatedSentence + '\n\n')

