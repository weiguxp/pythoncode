sumTarget =2
newIntList = [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0]

if sum(newIntList) > sumTarget:
	print "reduce 1"
	for i in range(len(newIntList)):
		if newIntList[i] > 0:
			newIntList[i] -= 1
			print sum(newIntList)
			# if sum(newIntList) == sumTarget : print "break"

print newIntList