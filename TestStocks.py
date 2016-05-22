from googlefinance import getQuotes
import json


# # TSLAstock = json.dumps(getQuotes('TSLA'), indent=2)

# TSLAstock = json.dumps(getQuotes('TSLA'), indent=2)

# print TSLAstock

# # stock = dict()
# # stock = json.loads(TSLAstock)

# # print type(stock)

# import json

# data = {
#    'name' : 'ACME',
#    'shares' : 100,
#    'price' : 542.23
# }

# json_str = json.dumps(data)

# print json_str 


# TSLAstock = json.dumps(getQuotes('TSLA'), indent=2)

# print TSLAstock

# stock = json.loads(TSLAstock)

# print stock 

quotes = json.loads(getQuotes('AAPL'))

print quotes[0]