from DailyRecord import *
from ParseDAU import *
from ParseIncome import *
import pylab
import datetime
import cPickle as pickle


recordList = ParseFileToDailyRecords('input.csv')
recordList2 = ParseIncomeFile('income.csv')

recordDict = {}

def AddToRecordDict(r):
	for record in r:
		dateSig = DateSignature(record.Date)

		try:

			if recordDict[dateSig].MAUData:
				print 'found MAU Record'

			if recordDict[dateSig].IncomeData:
				print 'found income data'
			else:
				print 'Adding income data for ', recordDict[dateSig].Date
				recordDict[dateSig].income = record.income
				recordDict[dateSig].IncomeData = True


			print 'found record'
		except KeyError:
			print 'adding record'
			recordDict[dateSig] = record



def AverageValues():
	sumDAU = 0.0
	for record in recordList:
		sumDAU += record.DAU

	print sumDAU, sumDAU/len(recordList)


def PlotTargetValue(valueS):
	DAUTally = []
	monthTally = []

	for record in recordDict:
		DAUTally.append(getattr(record, valueS))
		monthTally.append(record.Date)

	pylab.plot(monthTally, DAUTally)

def PlotTest():
	PlotTargetValue('DAU')
	PlotTargetValue('MAU')
	PlotTargetValue('WAU')
	PlotTargetValue('income')
	pylab.show()


def SaveRecordList():
	with open('RecordSave2.pk1', 'wb') as output:
		pickle.dump(recordList, output, -1)

def LoadRecordList():
	with open('RecordSave2.pk1', 'rb')  as input:
		listS = pickle.load(input)
		return listS

# SaveRecordList()

# recordList = LoadRecordList()

print recordList
print recordList[1]

AddToRecordDict(recordList)
AddToRecordDict(recordList2)
AddToRecordDict(recordList2)

print recordDict

PlotTest()