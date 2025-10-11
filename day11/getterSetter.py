class Student:
    def __init__(self,name,rollNo,age):
        self.name=name
        self._rollNo=rollNo
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        #we can also add some logic like age limit for update
        self.__age=age
    def __display(self):
        print(f"Hi myself {self.name} {self.__age} year old with roll no : {self._rollNo} from student class")
    def displayPrivateData(self):
        self.__display()

class Branch(Student):          #inheritance
    def show(self):
        print(f"My rollno is {self._rollNo}")

s1 = Student("Anurag",23,20)
print(s1._Student__age)
s1._Student__display()

print(s1.get_age())
s1.set_age(22)
print(s1.get_age())