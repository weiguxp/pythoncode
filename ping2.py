import urllib2
from HTMLParser import HTMLParser
import smtplib
from sparkpost import SparkPost
import time

sp = SparkPost('a0c04366cd1a5e02ac31f62e6ff4e9aa105afc2c')


def getReport(targetURL, numRetry = 0):
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
			getReport(targetURL, numRetry + 1)
	else:
		return 0

def sendErrorMail(mailMsg):
	response = sp.transmissions.send(
	    recipients=['weiguxp@gmail.com'],
	    html='<p>Automated Message</p>',
	    from_email='wei@weigu.org',
	    subject= mailMsg
	)
	print(response)

def monitorServers():
	totalUpStats = 0 
	totalUpStats += getReport('http://zhaoyun.sanguochong.com.cn/cluster/status')
	totalUpStats += getReport('http://mayiyx.sanguochong.com.cn/cluster/status')
	totalUpStats += getReport('http://7u6u.sanguochong.com.cn/cluster/status')
	totalUpStats += getReport('http://2686.sanguochong.com.cn/cluster/status')
	print 'got some Uptime reports, total is %i' % totalUpStats
	if totalUpStats != 12:
		sendErrorMail('Some clusters are down')


while 1 != 0 :
	print 'starting cycle'
	monitorServers()
	time.sleep(300)



