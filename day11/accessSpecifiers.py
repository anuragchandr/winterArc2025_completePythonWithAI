class Student:
    def __init__(self,name,rollNo,age):
        self.name=name
        self._rollNo=rollNo #protected
        self.__age=age #private
    def __display(self):
        print(f"Hi myself {self.name} {self.__age} year old with roll no : {self._rollNo} from student class")
    def displayPrivateData(self):
        self.__display()

class Branch(Student): #age cant be accesed here too
    pass
s1 = Student("Rahul",54,22)
b1 = Branch("Anurag",16,21)
print(b1._rollNo) #accessible

#print(s1.__age) # not accessible
print(s1._Student__age)
print(dir(s1))