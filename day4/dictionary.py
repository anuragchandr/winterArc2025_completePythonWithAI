mydict = { "name": "Anurag", "age": 20, "course": "ECE" }
print(type(mydict))

print(mydict["name"])
print(mydict.get("age"))

mydict["college"] = "Patna University" 
print(mydict)

mydict["age"] = 21            
print(mydict)

mydict.pop("course") 
print(mydict)

print(mydict.keys())      
print(mydict.values()) 
print(mydict.items())        

print(len(mydict))             
mydict.clear()            
print(mydict)
