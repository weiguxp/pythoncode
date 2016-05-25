import gaugette.ssd1306
import time
import sys
from googlefinance import getQuotes
import json

RESET_PIN = 15 # WiringPi pin 15 is GPIO14.
DC_PIN = 16 # WiringPi pin 16 is GPIO15.
led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
led.begin()
led.clear_display() # This clears the display but only when there is a led.display() as well!



def getStockPrice(ticker):
	StockPrice = json.dumps(getQuotes(ticker))
	TSLAstock = json.loads(StockPrice)[0]
	return TSLAstock['LastTradePrice']


def displayStock(ticker):
	price = getStockPrice('TSLA')
	output = ticker + " " + price
	return output
	
	


while 1 != 0:
	dispTime = time.strftime("%X")
	led.draw_text2(0,0,dispTime, 1)
	stockPrice = displayStock('TSLA')
	led.draw_text2(0,16,stockPrice,2)
	led.display()	
	time.sleep(10)
