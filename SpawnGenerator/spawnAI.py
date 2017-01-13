import math

def normpdf(x, mean, sd):
    var = float(sd)**2
    pi = 3.1415926
    denom = (2*pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def roundList(myList, sumTarget):
	#attempts to fix rounding problems
	#fixes sum of a list fit the sumTarget

	newIntList = []
	ratio = 1

	while (sum(newIntList) < sumTarget):
		newIntList = []
		for i in myList:
			newIntList.append(int(i*ratio))
		ratio += 0.05


	if sum(newIntList) > sumTarget:
		for i in range(len(newIntList)):
			if newIntList[i] > 0:
				newIntList[i] -= 1
				if sum(newIntList) == sumTarget: break

	return newIntList

def spawnBetween(tMin, tMax, sumTarget):
	#generates a list between two times
	tAverage = (float(tMin) + tMax) / 2
	tStdDev = (tMax - tMin) /4
	myList = []
	for i in range(tMin, tMax +1 ):
		# print str(i) + " , " + str(normpdf(i,tAverage,tStdDev))
		myList.append(normpdf(i,tAverage,tStdDev))
		#print myList
	myList = normList(myList, sumTarget)

	tupleList = []
	for i in range(len(myList)):
		tupleList.append((i+tMin, myList[i]))
	return tupleList


def normList(myList, sumTarget):
	#returns a list of integers with a sum = sumTarget
	listSum = sum(myList)
	ratio = sumTarget / listSum
	newList = []

	for i in myList:
		newList.append(i*ratio)
	newList = roundList(newList,sumTarget)
	return newList


# mySpawn = spawnBetween(42,50,2)
# print mySpawn