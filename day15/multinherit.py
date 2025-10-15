class Human:
    def __init__(self):
        self.num_eyes=2
    def speak(self):
        print("i'm sleeping")
    def work(self):
        print("i'm working")

class male:
    def __init__(self,age):
        self.age = age
    def flirt(self):
        print("I can Flirt")
    

class boy(Human,male):
    pass


b1 = boy()
print(b1.age)