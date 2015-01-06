import math
import random
import time
import bisect

myList = []
myListList = []


def AddRandom(n, l):
	for i in range (n):
		h = random.randint(1,100)
		l.append(h)

def SortList(l):
	h = 0
	while h < len(l)-1:
		if l[h] > l[h+1]:
			k = l[h]
			l[h] = l[h+1]
			l[h+1] = k
			h=0
		else:
			h +=1


def isSorted(l):
	for i in range(len(l)-1):
		print i
		if l[i] > l[i+1]:
			print l[i] , 'is larger than', l[i+1]
			return False
			break
	return True

def isAnagram(list1, list2):
	'''checks if a letter is in list2'''
	for letter in list1:
		if letter not in list2:
			print letter, list2
			return False
			break
	return True


def convertList(str):
	word2_list = []
	for letter in str:
		word2_list.append(letter)
	return	word2_list


def isDupe(l):
	for i in range(len(l)-1):
		if l[i] in l[i+1:]:
			# print l[i], 'found in ', l[i+1:]
			return True
	return False

def removeDupe(l):
	rmvList = []
	for i in range(len(l)-1):
		if l[i] in l[i+1:]:
			rmvList.append(l[i])
	for i in rmvList:
		l.remove(i)

def rand2dig(n):
	'''Returns a number in string form between 1 and n'''
	h = random.randint(1,n)
	if h < 10:
		return '0' + str(h)
	return str(h)


def simClass():
	testlist =[]
	for i in range(23):
		testlist.append(rand2dig(12)+rand2dig(30)) 
	# print testlist
	if isDupe(testlist)==True:
		return 1
	else:
		return 0

def simualteBirthday():
	h=0
	for i in range(1000):
		h += simClass()
	print float(h)/1000



def appendfile():
	"""returns the stripped version of words.txt"""
	t = []
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		t.append(word)
	return t


def measuretime(func,l):
	'''prints the amount of time it takes to perform function'''
	start_time = time.time()
	t = func(l)
	elapsed_time = time.time() - start_time
	print 'this operation took', elapsed_time, 'seconds'


def ReverseWord(word):
	return word[::-1]

def BinSearch2(target, l):
	'''Uses binary Search to find target in list l'''
	min = 0 
	max = len(l) - 1
	iterations = 10

	for i in range(iterations):
		if max - min <20: #stop searching when min and max have difference of less than 20
			break

		average = (min + max) /2
		if target > l[average]:
			min = average
		else:
			max = average

	# print min, max, l[min:max+1]
	if target in l[min:max+1]:
		return True
	else:
		return False

def PrintReversePair(l):
	for word in l:
		revword = ReverseWord(word)
		if BinSearch2(revword, l)==True:
			print word
			# fastList.append(word)

def PrintReversePairSlow(l):
	for word in l:
		revword = ReverseWord(word)
		if revword in l:
			print word
			slowList.append(word)

def findmissing():
	dupList = []
	fin = open('finddupe2.txt')
	for word in fin:
		myword = word.strip()
		dupList.append(myword)
	for i in range(len(dupList)/2):
		if dupList[i] not in dupList[i+1:]:
			print dupList[i]

# def BinSearch(min, max, l, target, iteration):
# 	'''print BinSearch(0 ,20, myList, 23, 2)'''
# 	if iteration < 1 :
# 		if target in l[min:max]:
# 			return True
# 		else:
# 			return False

# 	average = (max + min) / 2
# 	if target > l[average]:
# 		min = average
# 	else:
# 		max = average

# 	newi = iteration -1
# 	print min, max, newi
# 	return BinSearch(min, max, l, target, newi)
# AddRandom(40, myList)
# SortList(myList)
# print myList
# print BinSearch2(43,myList)


myList = appendfile()


def PrintReversePair3(l):
	for word in l:
		revword = ReverseWord(word)
		loc = bisect.bisect_left(l, revword)
		if loc != len(l) and l[loc]==revword:
			print word


def interlock(word1, word2):
	'''Interlocks the two inputted words'''

	if len(word1) > len(word2):
		print 'word 1 is longer'
		return 'Error'
	newWord =''
	for i in range(len(word1)):
		newWord += word1[i] + word2[i]
	return newWord

def FindAllLen(wordlength, l):
	newList =[]
	for word in l:
		if len(word) == wordlength:
			newList.append(word)
	return newList


def FindITL():
	myL = FindAllLen(4, myList)
	for word in myL:
		for word2 in myL:
			conj = interlock(word, word2)
			if BinSearch2(conj, myList)==True:
				print word, word2, conj

FindITL()







