class Human:
    def __init__(self,finger):
        self.num_eyes=2
        self.num_finger=finger
    def speak(self):
        print("i'm sleeping")
    def work(self):
        print("i'm working")

class male(Human):
    def __init__(self,finger):
        super().__init__(finger) #without this it will not inherit parent attributes
        self.age =4
    def work(self):
        super().work()
        print("i'm coding") #overriding

m1 = male(10)

m1.speak()
m1.work()

print(m1.num_finger)