import datetime



def LoadFile(myFile):
    ''' 
    Returns a List of Records using contents of myFile
    '''
    fin = open(myFile)

    CSVList = AddFileToLines(fin)
    return CSVList


def AddFileToLines(fin):
    myList = []
    for line in fin:
        myLine = line.strip()
        myLine = BreakCSV(myLine)
        myDate, MAU, WAU, DAU = myLine
        myRecord = DailyRecord(myDate, MAU, WAU, DAU)
        myList.append(myRecord)
    return myList

def BreakCSV(StrIn):
    ''' 
    StrIn: Finds commas and breaks into a list of strings 
    Returns a List
    '''

    myL = []
    myStr = ""
    StrIn += ','

    for letter in StrIn:
        if letter == ',':
            myL.append(myStr)
            myStr = ''
        else:
            myStr += letter
    return myL


class DailyRecord(object):
    ''' 
    Daily Reord of this date's important insights

    '''
    def __init__(self, myDate, MAU, WAU, DAU):
        self.myDate=str(myDate)
        self.MAU=int(MAU)
        self.WAU=int(WAU) 
        self.DAU=int(DAU)

    def __str__(self):
        return 'record date: %s, MonthlyUsers: %g, WeeklyUsers: %g, DAU: %g' % (self.myDate, self.MAU, self.WAU, self.DAU)

