from structshape import structshape
from ParseFile import *
import math
import time

myList = ParsePartF('words.txt',10000)
myFullList = ParseF('words.txt')
myDict = {}
myLenDict = {}
myRedDict = {}

for word in myFullList:
    myDict[word] = 1

def Histogram(word):
    ''' breaks down _word_ into letters and sorts them alphabetically
        returns a string
    '''
    myDict = {}
    for letter in word:
        myDict[letter] = myDict.setdefault(letter, 0) + 1

    myTupleList = []
    for element in myDict:
        myTupleList.append((element,myDict[element]))

    myTupleList.sort()

    stringout = ''.join(myTupleList)

    for letter, number in myTupleList:
            stringout += letter + str(number)
    return stringout


def SignatureWord(word):
    '''strips a word and forms a 'signature' of the word based on how the letters inside. used for anagrams'''
    myWord = word.strip().lower()
    myList = list(myWord)
    myList.sort()

    myWord = ''.join(myList)
    return myWord


def FindAnagrams(l):
    myDict = {}

    for word in l:
        wordKey = SignatureWord(word)
        try:
            myDict[wordKey] += [word]
        except KeyError:
            myDict[wordKey] = [word]

    myList = []

    for key in myDict:
        numAnag = len(myDict[key])
        if numAnag > 1:
            numLetters = len(myDict[key][0])
            myList.append((numAnag, numLetters, myDict[key]))

    myList.sort(reverse = True)
    return myList

print FindAnagrams(myFullList)


def NumSwaps(w1, w2):
    ''' returns number of letter swaps anagrams w1, w2'''
    numSwap = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            numSwap +=1
    return numSwap

def FindMetaPair():
    anagList = FindAnagrams(myList)
    metaPair = []
    for x, y, wordlist in anagList:
        for word1 in wordlist:
            for word2 in wordlist:
                if word1 < word2 and NumSwaps(word1, word2) == 2:
                    print word1, word2
 
def CheckInDict(word, *args):
    if args:
        target = args[0]
    else:
        target = myDict

    if word in target:
        return True
    return False


def ReduceWord(word):
    myList = []
    for i in range(1,len(word)+1):
        newWord = word[:i-1] + word[i:]
        if CheckInDict(newWord) == True:
            myList.append(newWord)
    return myList


def RecurReduceable(word):
    if len(word) ==1:
        return True
    rWords = ReduceWord(word)
    if not rWords:
        return False
    for arWord in rWords:
        if RecurReduceable(arWord) == True:
            return True
    return False





def BuildmyLenDict():
    for word in myFullList:
        wordLength = len(word)
        try:
            myLenDict[wordLength] += [word]
        except KeyError:
            myLenDict[wordLength] = [word]


def BuildReducableWords():
    BuildmyLenDict()

    for word in myLenDict[1]:
        myRedDict[word] = 1


    for i in range (2,18):
        for word in myLenDict[i]:
            # print 'searching word', word,
            for redWord in ReduceWord(word):
                # print redWord
                if CheckInDict(redWord, myRedDict) == True:
                    # print 'adding', word
                    myRedDict[word] = 1

def BuildReducableWords2():
    for word in myFullList:
        if RecurReduceable(word)== True:
            myRedDict2[word] = 1

def test2():
    myRedDict2 = {}

    t1 = time.time()
    BuildReducableWords()
    t2 = time.time()
    BuildReducableWords2()
    t3 = time.time()

    m1time = t2 - t1
    m2time = t3 - t2
    print 'building method time =', m1time ,'found=', len(myRedDict), 'recursion method time =', m2time , 'found =', len(myRedDict2)