class Human:
    def __init__(self, name, age):
        print("Parent class initialized")
        self.name = name
        self.age  = age
    def sleep(self):
        print("Sleepig...Zzzzz")
    
class Female(Human):
    def __init__(self, name, age, hobby):
        print("Child class triggered.")
        super().__init__(name, age)
        self.hobby = hobby
    def sleep(self):
        super().sleep()
        print("Snoring")
    def walk(self):
        print(f"And {self.name} goes matching on!")

mercy = Female("Mercy", 25, "Swimming")
print(mercy.name)
print(mercy.age)
mercy.sleep()
mercy.walk()