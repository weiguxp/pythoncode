import datetime

def ParseDate(stringS):
    monthS, dateS, yearS = BreakSeparator(stringS, '/')
    dateDate = datetime.date(int(yearS), int(monthS), int(dateS))
    return dateDate

def BreakSeparator(StrIn, *args):
    ''' 
    StrIn: Finds separator and breaks into a list of strings 
    Optional: specify the separator
    Returns a List
    '''
    if args:
        separator = args[0]
    else:
        separator = ','
    listS = []
    acumString = ""
    StrIn += separator

    for letter in StrIn:
        if letter == separator:
            listS.append(acumString)
            acumString = ''
        else:
            acumString += letter
    return listS

def DateSignature(dateS):
    return dateS.isoformat()