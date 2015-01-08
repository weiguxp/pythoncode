import datetime
from ParserWei import *
from DailyRecord import *


def ParseIncomeFile(myFile):
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
    dateStr, incomeS = lineS
    dateDate = ParseDate(dateStr)
    recordS = DailyRecord(dateDate)
    recordS.IncomeData = True

    if incomeS == '-':
        incomeS = 0.0

    recordS.income = float(incomeS)

    
    return recordS


