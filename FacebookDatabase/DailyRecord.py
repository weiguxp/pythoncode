class DailyRecord(object):
    ''' 
    Daily Reord of this date's important insights

    '''
    def __init__(self, myDate):
        self.Date = myDate
        self.MAUData = False
        self.IncomeData = False

    def __str__(self):
        return 'record date: %s, MonthlyUsers: %g, WeeklyUsers: %g, DAU: %g' % (self.Date, self.MAU, self.WAU, self.DAU)

    def __repr__(self):
        return 'Record%s' % self.Date
