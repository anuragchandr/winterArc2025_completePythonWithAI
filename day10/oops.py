#class
class Human: 
    gender="male"

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def talk(self):
        print(f"Hello I am {self.name} and my age is {self.age}")
    

man1 = Human("Ram",25) #object creation -- instance of class

print(man1.gender)
print(man1.age)
man1.talk()
