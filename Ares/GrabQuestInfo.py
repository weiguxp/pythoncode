import xlwt
import xlrd
import os
import glob

from datetime import datetime

files = glob.glob("*.xlsx")


def FilterStage(stagedump):
	if 'Stage' in stagedump:
		return stagedump
	else:
		return ' '

def FindStr(worksheets, trgRow, mystr):
	num_rows = worksheets.nrows
	for i in range(num_rows):
		if worksheets.cell(i, trgRow).value == mystr:	
			return i
	return 0


def GrabXlsData(bookname):
	readworkbook = xlrd.open_workbook(bookname)
	worksheet = readworkbook.sheet_by_index(0)

	questname = worksheet.cell(2, 1).value
	displayname = worksheet.cell(2, 2).value
	minlevel = worksheet.cell(2, 4).value
	questdesc = worksheet.cell(2, 5).value
	actiontype = worksheet.cell(26, 10).value
	actiontext = worksheet.cell(26, 11).value
	stagedump = worksheet.cell(26, 4).value
	stagenumber = FilterStage(str(stagedump))
	addexp = worksheet.cell((FindStr(worksheet, 2, 'Exp')), 3).value 
	addmoney = worksheet.cell((FindStr(worksheet, 2, 'Money')), 3).value 

	return questname, displayname, minlevel, questdesc, actiontype, actiontext, stagenumber, addexp, addmoney




def GenBookName(booknum):
	if booknum < 10:
		return 'Act01Main00' + str(booknum) + '.xlsx'
	else:
		return 'Act01Main0' + str(booknum) + '.xlsx'



wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')


#write title
title = 'questname', 'displayname', 'minlevel', 'questdesc', 'actiontype', 'actiontext', 'stagenumber', 'addexp', 'addmoney'
for j in range (9):
	ws.write(0 , j, title[j])


for i in range (207):
	dumpedData = GrabXlsData(files[i])
	print dumpedData
	for j in range (9):
		ws.write(i + 1 , j, dumpedData[j])





wb.save('QuestDump.xls')