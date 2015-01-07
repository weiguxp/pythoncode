import math
import random
from bisect import bisect_left

def FileToList(filename):
    '''returns a list with the contents of filename'''
    fin = open(filename)
    targList = []
    for line in fin:
        word = line.strip()
        targList.append(word)
    return targList

def SeparateWord(word):
    Even = word[::2]
    Odd = word[1::2]
    return Even, Odd

def BisSearch(word_list, word):
    i = bisect_left(word_list, word)
    if i != len(word_list) and word_list[i] == word:
        return True
    else:
        return False

def interlockSearch():
    for word in myList:
        Even, Odd = SeparateWord(word)
        if BisSearch(myList, Even)==True and BisSearch(myList, Odd)==True:
            print Even, Odd, word


# myList = FileToList('words.txt')

# interlockSearch()

def FunRescur(myString, tally, itn):
    if itn > 0 :
        if tally > 0:
            FunRescur(myString + ')', tally -1, itn -1)
        FunRescur(myString + '(', tally +1, itn -1)
    if tally==0 and itn == 0:
        print myString

FunRescur('', 0, 6)
