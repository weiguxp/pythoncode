import math
import random

myList = []
myListList = []
fin = open('words.txt')

def AddRandom(n, l):
	for i in range (n):
		h = random.randint(1,10)
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

def RemoveElements(n,l):
	print 'popping the following numbers:'
	for i in range(n):
		print 'l[', i, '] =', l.pop(),
	print 'new length of list is ', len(l)


def PrintList():
	print 'Length of List is ' , len(myListList)
	print myListList

def Middle(l):
	l.pop()
	del l[0]

def isSorted(l):
	for i in range(len(l)-1):
		print i
		if l[i] > l[i+1]:
			print l[i] , 'is larger than', l[i+1]
			return False
			break
	return True

def isAnagram(list1, list2):
	for letter in list1:
		if letter not in list2:
			print letter, list2
			return False
			break
	return True


def isAnagram2(word1, word2):
	word2_list = convertList(word2)

	for letter in word1:
		if letter in word2_list:
			word2_list.remove(letter)
		else:
			return False

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

def simClass():
	h=0
	for i in range(1000):
		h += simClass()
	print float(h)/1000

wordlist1 = []

def appendfile():
	for line in fin:
		word = line.strip()
		wordlist1.append(word)

appendfile()