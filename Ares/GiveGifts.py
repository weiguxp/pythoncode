import requests


# payload = {'worldId':'1','giftId':'wechat', 'giftCount':'1'}

payload = {'userId': '107', 'worldId':'0', 'command':'AddGameItem','itemId':'gemMagicT1','amount':'1'}
url_2 = 'http://139.196.192.2:10000/msgToUser'

# req = requests.post(url_2, data=payload)

print type()
print req.text 
