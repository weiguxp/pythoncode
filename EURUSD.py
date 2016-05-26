from googlefinance import getQuotes
import json



sentEmails = 1

def testemails():
	global sentEmails
	sentEmails += 1
	print sentEmails

testemails()
testemails()