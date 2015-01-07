import math
import random

myList = []

def insertrandom(n, l):
	for i in range(n):
		h = random.randint(0,100)
		l.append(h) 

def insertranlist(l):
	tempList = []
	insertrandom(10, tempList)
	l.append(tempList)


def sortList(tarList):
	p = 0
	while p < len(tarList) -1:
		nestedFunc(tarList[p+1], sortList)
		if tarList[p] > tarList[p+1]:
			h = tarList[p]
			tarList[p] = tarList[p+1]
			tarList[p+1] = h
			p = 0
		else:
			p+=1

def isList(v):
	if type(v) is list:
		return True
	else:
		return False

def sumAll(v):
	tempSum = 0
	for i in v:
		tempSum += nestedFunc(i, sumAll)

	return tempSum

def nestedFunc(i, func):
	if isList(i) == True:
		return func(i)
	else:
		return i



insertrandom(10, myList)
insertranlist(myList)
insertranlist(myList)

isList(myList[9])

sortList(myList)

print sumAll(myList)

print myList