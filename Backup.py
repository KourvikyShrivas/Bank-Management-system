#oops
'''class Hello:
    a =12
    def speak(self):
        print(self)
        print("how are you")

obj = Hello() #created in object  ,object pass their location
print (obj.a) #object can also access attribute
obj.speak()   #when we use objectss to call any method
              #inside class we always send location of my object'''


#constructor ka kaam hota hai input lena 
#it is a method
#in python constructor is know as initializer
'''class Factory:  
   def __init__(self):  #self function  is called whenever a newobject is created and this self will 
                         #target the location of your object 
        print ("how are you")
        print("this is p23 batch")

a = Factory()
b = Factory()
c = Factory()'''


#2nd use of constructor function
'''class Factory:
    def __init__(self,zips,pockets,material):
        self.zips = zips
        self.pockets = pockets
        self.material = material

    def details(self):
        print("Your bag details are :-")
        print(self.zips)
        print(self.pockets)
        print(self.material)

reebok = Factory(2,2,"Leather")

campus = Factory(4,2,"plastic")

print(campus.material)'''


#classes and attributes
#methods are also overwritten
'''class Registration:
    age =18 #class attribute
    def __init__(self,name,email,age,number):
        if age >= Registration.age:
            self.name = name   #object attribute
            self.email = email
            self.number = number
        else:
            print("you cannot register you are underage")
            return
        
    def details(self): #object method - it targets the location of object
        print(self.name) #self will take the location of the object 
        print(self.email) #whichever object is calling
        print(self.number)
        print(self.number)
        print(self.age)

    @classmethod
    def dummy_details(cls):#class method -it will always access the location of your class
        print(cls.name) 
        print(cls.email) 
        print(cls.number)
        print(cls.number)
        print(cls.age)

    @staticmethod #static method 
    def college_details(): #this method will not target any location
        print("I will notteach you anything" \
              "and I will not teach you anything" \
                "welcome to reaal world")

Student1=Registration("Harsh","harsh@gmail.com",21,1234567890)

Student1.dummy_details()'''



#inheritance 
#one class attribute and methods can be accessed by another class this thing is known as inheritance 
'''class BhopalFactory:
    Reg_num = 12345678909 #class method
    def __init__(self,color,size,type): #__init__kind of method
        self.color = color
        self.size = size
        self.type = type

    def details(self): #object method
        print("Your shoes details are : ")
        print(self.color)
        print(self.size)
        print(self.type)
class Indoreoutlet(BhopalFactory):
    def __init__(self, color, size, type, price):
        super().__init__(color, size, type)  #super class methods and attributes of parent class means it its placewe can also write 
                                              #bhopalfactory but there you have to write the self also means it will require positional argument
        self.price = price
shoe1 = BhopalFactory("Red",8,"Jordan")
shoe2 = Indoreoutlet("Yellow",7,"Sneakers",1000)'''


'''class Animal:
    def __init__(self,name):
        self.name = name
class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self):
        print("hello human you speak")

class Robot(Animal,Human):
    def __init__(self,name,age):
        super().__init__(self,name,age)
        
obj = Robot("Alpha1",2)  #yha pr abhi error hai 



#hierarchical inheritance
class Animal:
    pass
class Human:
    pass
class Robot:
    pass


#hybrid inheritance
class Animal:
    pass
class Human:
    pass
class Robots(Animal,Human):
    pass
class AI(Robot):
    pass'''



#POLYMORPHiMS
'''class Animal:
    name ="lion"
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def detail(self):
        print("the details are: ")
        print(self.name)
        print(self.age)

class Human:
    name ="Harsh"

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def details(self):
        print("the details are: ")
        print(self.name)
        print(self.age)
        print(self.gender)

obj1 = Animal("giraffe",6)
obj2 =  Human("harsh",23,"male")

obj1.detail()
obj2.detail()'''


'''class BhopalFactory:
    Reg_num = 12345678909 #class method
    def __init__(self,color,size,type): #__init__kind of method
        self.color = color
        self.size = size
        self.type = type

    def details(self): #object method
        print("Your shoes details are : ")
        print(self.color)
        print(self.size)
        print(self.type)
class IndoreFactory(BhopalFactory):
    def __init__(self, color, size, type, price):
        super().__init__(color, size, type)  #super class methods and attributes of parent class means it its placewe can also write 
                                              #bhopalfactory but there you have to write the self also means it will require positional argument
        self.price = price

    def details(self):
        print (super().details())
        print(self.price)
obj = IndoreFactory("red",8,"jordan",18000)
obj.details()

#this obj can now only call one method that is of IndoreFactory 
#it cannot call BhopalFactory detail method
#and this thing is known as method overriding'''


#method overloading
'''class Animal:
    def hello():
        pass
    def hello(a,b):
        pass
obj = Animal()
obj.hello(12,45)

#samme name methods inside a single class but with different parameters
#this thing is known as method overloading
#but it is not available in python'''



#Encapsulation
#protecting attribute and methods
class Animal:
    a  = 12 #public attribute
    _b = 23 #protected attribute
    __c =22 #private method
    def hello(self): #public method
        print("how are you")
    def hello2(self): #protected method
        print("how are you 2")
    @classmethod 
    def __hello3(self):
        print("how are you 3") #private method
obj = Animal()
print(obj.a)


#Abstraction
from abc import ABC, abstractmethod
class person(ABC):
    @abstractmethod
    def info():
        pass
    @abstractmethod
    def register():
        pass

class Teacher(person):
    def info():
        pass
    def register():
        pass
class Students(person):
    def info():
        pass
    def register():
        pass
obj = Students()        