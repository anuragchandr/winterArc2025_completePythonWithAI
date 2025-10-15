class Human:
    def __init__(self):
        self.num_eyes=2
    def speak(self):
        print("i'm sleeping")
    def work(self):
        print("i'm working")

class male(Human):
    def work(self):
        super().work()
        print("i'm coding") #overriding

m1 = male()

m1.speak()
m1.work()