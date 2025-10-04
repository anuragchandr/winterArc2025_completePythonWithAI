myset = { "apple", "banana", "cherry" }
print(type(myset))

myset.add("grape")  
print(myset)

myset.update(["orange", "kiwi"]) 
print(myset)

myset.remove("banana")     
print(myset)

myset.discard("cherry") 
print(myset)

print(len(myset))          
myset.clear()  
print(myset)
