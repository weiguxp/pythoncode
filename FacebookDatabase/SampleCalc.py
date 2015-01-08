from ParseDAU import *
import pylab
myList = LoadFile('input.csv')

def AverageValues():
	sumDAU = 0.0
	for record in myList:
		sumDAU += record.DAU

	print sumDAU, sumDAU/len(myList)


def PlotValues():
	DAUTally = []

	for record in myList:
		DAUTally.append(record.DAU)

	Pylab.plot(DAUTally)
	Pylab.show()

PlotValues()