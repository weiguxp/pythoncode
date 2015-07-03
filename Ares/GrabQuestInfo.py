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

	questname = worksheet.cell(2, 1).value
	displayname = worksheet.cell(2, 2).value
	minlevel = worksheet.cell(2, 4).value
	questdesc = worksheet.cell(2, 5).value
	actiontype = worksheet.cell(26, 10).value
	actiontext = worksheet.cell(26, 11).value
	stagedump = worksheet.cell(26, 4).value
	stagenumber = FilterForWord(str(stagedump), 'Stage')
	addexp = worksheet.cell((FindStr(worksheet, 2, 'Exp')), 3).value 
	addmoney = worksheet.cell((FindStr(worksheet, 2, 'Money')), 3).value 


	convoList = []
	convo = []
	chatStart = FindStr(worksheet, 1, 'questChatList') +2
	convoRow= 0
	while worksheet.cell(chatStart + convoRow, 1).value != "":

		selectRow = chatStart + convoRow
		qId = worksheet.cell(selectRow, 1).value 
		qobjectType = worksheet.cell(selectRow, 2).value 
		qidentify = worksheet.cell(selectRow, 3).value 
		qanimation = worksheet.cell(selectRow, 4).value 
		qChat = worksheet.cell(selectRow, 5).value 

		convo = qId, qobjectType, qidentify, qanimation, qChat
		convoList += [convo]
		convoRow += 1 

	print convoList


	rList = questname, displayname, minlevel, questdesc, actiontype, actiontext, stagenumber, addexp, addmoney, convoList
	return rList


files = glob.glob("*.xlsx")


wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')


#write title
title = 'questname', 'displayname', 'minlevel', 'questdesc', 'actiontype', 'actiontext', 'stagenumber', 'addexp', 'addmoney'
for j in range (9):
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
wb.save('QuestDump.xls')