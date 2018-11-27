#Using Class name inherit the composition of one class into another class

class Engine:
    a=10 #static variable
    def __init__(self): #constructor
        self.b=10 #properties
    def m1(self):#Instance method
        print("This is Engine class")
        print("The value of property 'b'=> ",self.b)
        print("The value of static variable in Engine class using 'self'=> ",self.a)
        print("The value of static variable in Engine class using 'class name'=> ",Engine.a)
class Car:
    def __init__(self,CarName,Model):
        self.c=30
        self.car=CarName
        self.model=Model
        self.e=Engine() #Using Class Name inherite all the properties and method
    def m2(self):
        print("Car Name=> ",self.car)
        print("Car Model=> ",self.model)
        self.e.m1()

c=Car("Phantom","Top_Model")
c.m2()
