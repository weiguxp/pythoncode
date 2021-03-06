import datetime
from ParserWei import *
from DailyRecord import *


def ParseFileToDailyRecords(myFile):
    ''' 
    Returns a List of Records using contents of myFile
    '''
    fin = open(myFile)

    recordList = []
    for line in fin:
        recordList.append(ParseLineAsRecord(line))
    return recordList

def ParseLineAsRecord(stringS):
    lineS = stringS.strip()
    lineS = BreakSeparator(lineS, ',')  
    dateStr, MAU, WAU, DAU = lineS
    dateDate = ParseDate(dateStr)
    recordS = DailyRecord(dateDate)
    recordS.MAU=int(MAU)
    recordS.WAU=int(WAU) 
    recordS.DAU=int(DAU)
    recordS.MAUData = True

    return recordS



