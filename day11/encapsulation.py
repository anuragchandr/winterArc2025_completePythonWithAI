class Student:
    def __init__(self,name,rollNo,age):
        self.name=name
        self._rollNo=rollNo
        self.__age=age
    def __display(self):
        print(f"Hi myself {self.name} {self.__age} year old with roll no : {self._rollNo} from student class")
    def displayPrivateData(self):
        self.__display()

class Branch(Student):
    def show(self):
        print(f"My rollno is {self._rollNo}")

b1 = Branch("Nisha",45,22)
b1.show

#b1 = Branch("Bikash",22)
print(b1.name)

s1 = Student("Anurag",23,20)
print(s1._Student__age)
s1._Student__display()
#print(s1.__age) --Error

# Python doesnt totally resstrict from accesing private data its programmers duty to not modify it in program