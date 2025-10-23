# DAY 23

## Working with structured files

- ### JSON:

```python
import json
with open("data.json","w", encoding="utf-8") as f:
    json.dump(obj, f, indent=2)
with open("data.json","r", encoding="utf-8") as f:
    obj = json.load(f)
```

- ### CSV:

```python
import csv
with open("out.csv","w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name","age"])
    writer.writerows([["alice",30],["bob",25]])
```

### Exceptions & safe cleanup

- Use with to avoid needing finally to close files.
- If not using with, ensure f.close() in finally:

```python
f = open("x.txt")
try:
    ...
finally:
    f.close()
```

### Performance tips

- Stream large files (iterate) instead of using read() into memory.
- Use buffering (default) or specify buffer size in open(..., buffering=N) when needed.

## Sample code for __JSON__ handling

```python
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


```