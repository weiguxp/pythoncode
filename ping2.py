import urllib2
from HTMLParser import HTMLParser
import smtplib
from sparkpost import SparkPost
import time
from datetime import datetime
import requests
import base64

#Settings for Email / SMS posting
sp = SparkPost('a0c04366cd1a5e02ac31f62e6ff4e9aa105afc2c')
SMSpassword = base64.b64encode('123QWEasd')

def sendSMS(targetnumber,errorMSG):
	#Sends an SMS to target, notifying servers are down
	try:
		SMSHTTPPOST = 'http://61.147.98.117:9001/servlet/UserServiceAPI?method=sendSMS&isLongSms=0&username=18802671838&password=%s &smstype=1&extenno=123&mobile=%s&content=%s' % (SMSpassword, targetnumber, errorMSG)
		req = requests.get(SMSHTTPPOST)
		print req.text 
	except:
		print 'Error, cannot send SMS'

def sendErrorMail(mailMsg):
	#Send an error email using SparkPost
	try:
		response = sp.transmissions.send(
		    recipients=['weiguxp@gmail.com'],
		    html='<p>Automated Message</p>',
		    from_email='wei@weigu.org',
		    subject= mailMsg
		)
		print(response)
	except:
		print 'error cannot send email'


def getReport(targetURL, numRetry = 0):
	#Queries the targetURL and returns the number of servers "UP"
	#Retries a max of 3 times before returning 0
	if numRetry < 3:
		try:
			response = urllib2.urlopen(targetURL)
			html = response.read()
			myLine = html.split(" ")
			totalUp = 0
			for word in myLine:
				if word == "Up)":
					totalUp += 1
			return totalUp
		except:
			#Logs the retry attempt
			print 'retrying %s' %targetURL
			time.sleep(5)
			return getReport(targetURL, numRetry + 1)
	else:
		return 0

def monitorServers():
	#Monitors the servers, notifies if the number of servers is incorrect
	totalUpStats = 0 
	totalUpStats += getReport('http://zhaoyun.sanguochong.com.cn/cluster/status')
	totalUpStats += getReport('http://mayiyx.sanguochong.com.cn/cluster/status')
	totalUpStats += getReport('http://7u6u.sanguochong.com.cn/cluster/status')
	totalUpStats += getReport('http://2686.sanguochong.com.cn/cluster/status')
	print 'got some Uptime reports, total is %i' % totalUpStats
	if totalUpStats != 12:
		sendErrorMail('Some clusters are down')
		sendSMS(13084686372, 'some servers are down')
		sendSMS(15014090802, 'some servers are down')



while 1 != 0 :
	print 'starting cycle %s ' %str(datetime.now())
	monitorServers()
	time.sleep(300)



