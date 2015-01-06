import math

myString = 'hello world this is wei!'
fibDict = dict()
fibDict = {0:0, 1:1}

def SumAll(*args):
	'''Sums any number of arguments'''
	TempSum = 0.0 
	for i in args:
		TempSum += i
	return TempSum

eng2ch = dict()
eng2ch = {'one':'nihao', 'two' : 'er', 'three':'san'}

def histogram(s):
	myDict = dict()
	for letter in s:
		myDict[letter] = myDict.get(letter, 0) + 1
	return myDict

def PrintHist(h):
	'''Print keypairs in reverse alphabetical order'''
	myList = h.keys()
	myList.sort()
	revList = myList[::-1]
	for key in revList:
		print key, h[key]
	print myList

def RevLookup(h, v):
	myList = []
	for i in h:
		if h[i] == v:
			return i
	raise ValueError

def InvertDict(d):
	revDict = dict()
	for k in d:
		val = d[k]
		if val in revDict:
			revDict[val].append(k)
		else:
			revDict[val] = [k]

	return revDict

def Fibonacci(n):
	if n in fibDict:
		return fibDict[n]
	res = Fibonacci(n-1) + Fibonacci(n-2)
	fibDict[n] = res
	return res 


ackCount = {}
myCounter = 0

def Ack(m,n):
	# global myCounter
	# myCounter += 1

	if (m, n) in ackCount:
		print 'found'
		return ackCount[m,n]
	if m == 0:
		ackCount[m,n] = n+1
	if n==0 and m>0:
		ackCount[m,n] = Ack(m-1, 1)
	if m>0 and n>0:
		ackCount[m,n] = Ack(m-1, Ack(m,n-1))
	return ackCount[m,n]


Ack(3,3)


print ackCount
