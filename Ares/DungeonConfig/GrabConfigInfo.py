import xlwt
import xlrd
import os
import glob

from datetime import datetime


def FilterForWord(stagedump, findword):
	#Finds findword and returns stagedump, else returns empty string
	if findword in stagedump:
		return stagedump
	else:
		return ' '

def FindStr(worksheets, trgRow, mystr):
	#Finds a string in the target row of a worksheet. 
	# Returns a Row number if found 
	#returns 0 if row not found
	num_rows = worksheets.nrows
	for i in range(num_rows):
		if worksheets.cell(i, trgRow).value == mystr:	
			return i
	return 0


def GrabXlsData(bookname):
	#opens the file bookname and grabs data from the first sheet
	#returns a list with the files
	rList = []
	readworkbook = xlrd.open_workbook(bookname)
	worksheet = readworkbook.sheet_by_index(0)

	questname = worksheet.cell(1, 0).value
	questIndex = worksheet.cell(1, 1).value
	displayName = worksheet.cell(1, 2).value
	questDesc = worksheet.cell(1, 3).value
	energyCost = worksheet.cell(1, 4).value
	minLevel = worksheet.cell(1, 5).value
	stageFSM = worksheet.cell(1, 6).value
	dungeonType = worksheet.cell(1, 10).value
	stageEXP = worksheet.cell((FindStr(worksheet, 1, 'Exp')), 2).value 
	#dungeonType = FilterForWord(str(stagedump), 'Stage')



	# convoList = []
	# convo = []
	# chatStart = FindStr(worksheet, 1, 'rewards') +2
	# convoRow= 0
	# while worksheet.cell(chatStart + convoRow, 1).value != "":

	# 	selectRow = chatStart + convoRow
	# 	qId = worksheet.cell(selectRow, 1).value 
	# 	qobjectType = worksheet.cell(selectRow, 2).value 
	# 	qidentify = worksheet.cell(selectRow, 3).value 
	# 	qanimation = worksheet.cell(selectRow, 4).value 
	# 	qChat = worksheet.cell(selectRow, 5).value 

	# 	convo = qId, qobjectType, qidentify, qanimation, qChat
	# 	convoList += [convo]
	# 	convoRow += 1 

	# print convoList


	rList = questname, questIndex, displayName, questDesc, energyCost, minLevel, stageFSM, dungeonType , stageEXP, 'dummydata'
	return rList


files = glob.glob("*.xlsx")


wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')


#write title
title = 'questname' ,'questIndex' ,'displayName' ,'questDesc' ,'energyCost' ,'minLevel' ,'stageFSM' ,'dungeonType', 'stageEXP'
for j in range (len(title)):
	ws.write(0 , j, title[j])


# start writing stuff 

selectRow = 1
for i in range (len(files)):
	dumpedData = GrabXlsData(files[i])
	print dumpedData
	for j in range (len(dumpedData)-1):
		ws.write(selectRow, j, dumpedData[j])

	# convoList = dumpedData[9]
	# print convoList

	# for i in range (len(convoList)):

	# 	selectRow += 1
	# 	convo = convoList[i]
	# 	for j in range(len(convo)):
	# 		ws.write(selectRow, j, convo[j])

	# print 'length ' , len(convoList)
	# print convoList
	selectRow += 1




#Saves the workbook as questdump
wb.save('configDump.xls')