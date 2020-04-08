##my_dic={'key1':'value1,'key2':'value2}
prices_lookup={'apple':3.44,"organes": 'two dollars','milk': {'indemand':5.56},'choco':['a','b','c']}
print(prices_lookup['organes'])
print(prices_lookup['milk'])
print(prices_lookup['choco'][2].upper())
prices_lookup['bingo']='3'
print(prices_lookup)
print(prices_lookup.keys())
print(prices_lookup.values())
print(prices_lookup.items())