'''class SharmaVishnu: #Bleprint of object
    a = "lolo"  #class keandar variable -> Attributes

    def sample(): #class ke and ke function -> Methods
        print('This is a sample function')

SharmaVishnu.sample()
print(SharmaVishnu.a)

'''

'''class Animal:
    #Attribute 
    name ="Animal"

    #Methods
    def greet(self): #ki jab bhi class ke andar ke function ko object ki help se call karoge tou ek PARAMETER 
        set krna hoga
        print("This is Animal Class")

cat = Animal()  #here tau is an object
cat.greet()
print(cat.name)
#Object ka naam same as hota hai as name of the variable

'''

#create a class which will perform 2 task:
#1. greet the user -> "This is -----  Class"
#2. adding up two numbers
'''class Scorpio:
    def greet(self):
        print("This is a greet attribute")

    def add(self):
        a=10
        b=10
        print(a+b)
obj = Scorpio()
obj.greet()
obj.add()



'''




#constructor -> def __init__(dunder method)
#constructor sabse pehlr execute hone wale functions hai doesnt mater inke upar ya neeche koi function present hai
'''class SharmaVishnu:
    def __init__(self,name,age):
        self.name=name  #innstance attribute
        self.age =age
        print ("This is a constructor function")
    def menu(self):
        print(self.name)
        print(self.age)
        print("Paneer Kulche")
obj =SharmaVishnu("Amit",21)
obj.menu()
'''

#make a class which  will take 2 numbers as input create 1. 2 instance attribute
#2 createa function which will print greatest amoong them
'''class hulk:
    def __init__(self,a,b):
        self.a = a
        self.b= b
        print("This is a constructor")
    def large(self):
        if self.a > self.b:
            print(self.a, "is smallest")
        else:
            print(self.b ,"is greatest")
obj = hulk(10,12)
obj.large()'''


