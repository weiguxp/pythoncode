import requests
import base64


SMSpassword = base64.b64encode('123QWEasd')
print SMSpassword

# content = 'Testing 123'
# url_2 = 'http://61.147.98.117:9001/servlet/UserServiceAPI?method=sendSMS&isLongSms=0&username=18802671838&password=%s &smstype=1&extenno=123&mobile=13084686372&content=%s' % (SMSpassword, content)

# req = requests.get(url_2)
# print req.text 

http://61.147.98.117:9001/servlet/UserServiceAPI?method=sendSMS&isLongSms=0&username=18802671838&password=MTIzUVdFYXNk &smstype=1&extenno=123&mobile=13084686372&content=ServerDown