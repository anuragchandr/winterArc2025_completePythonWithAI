import json

data = '{"var1":"anurag", "var2":"Chandra"}'
parsed = json.loads(data)   #{'var1': 'anurag', 'var2': 'Chandra'}
print(parsed)
print(parsed['var1'])
print(type(parsed)) #dict
print(data) #{'var1': 'anurag', 'var2': 'Chandra'}
#print(data['var1']) #its a string not json


#load- from file    and loads - from string
#json.dump - make it js compatible

data2 = {
    "ChannelName": "shortcircuits",
    "cars": ['bmw','audi','ferrari'],
    "fridge": ('roti','bidi'),
    "isBad": False
}

jscomp = json.dumps(data2)
print(jscomp)

