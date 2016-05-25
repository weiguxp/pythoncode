from googlefinance import getQuotes
import json

def getStockPrice(ticker):
	StockPrice = json.dumps(getQuotes(ticker))
	TSLAstock = json.loads(StockPrice)[0]
	return TSLAstock['LastTradePrice']


print getQuotes('EURUSD')