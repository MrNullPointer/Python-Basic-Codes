import numpy as np
import datetime

class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,newAge):
        self.age = newAge
    def set_name(self,newName):
        self.name = newName
    def __str__(self):
        return "Animal :" + str(self.age) + "Name: " + str(self.name)
    
class Cat(Animal):
    def speak(self):
        print("meow!!!!")
    def __str__(self):
        return "Cat :" + str(self.name) + " Age " + str(self.age)

class Rabbit(Animal):
    tag = 1
    def __init__(self,name,age,parent1 = None,parent2 = None):
        self.name = name
        self.age = age
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabbit: " + str(self.name) + " " + str(self.age)
    def __add__(self,other):
        return Rabbit('Mopsy',0,self,other)
    def __eq__(self,other):
        parents_same = self.parent1 == other.parent1 and self.parent2 == other.parent2
        parents_opposite = self.parent1 == other.parent2 and self.parent2 == other.parent1
        return parents_same or parents_opposite
    
class Person(object):
    def __init__(self,name):
        '''This function only requires a name'''
        self.name = name
        self.birthday = None
        self.lastname = name.split()[-1]
    
    def getLastName(self):
        return self.name.split()[-1]
        
    def setbirthday(self,month,day,year):
        '''This function requires birthday for a person'''
        self.birthday = datetime.date(year,month,day)
        
    def age(self):
        '''This function gives the current age of person'''
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __str__(self):
        return "The persons name is: " + self.name + " and his age is: " + str(self.age())
    
#   
#
#Defining MIT Person class:
#
#
#
#
class MITPerson(Person):
    nextIDNum = 0
    
    def __init__(self, name):
        Person.__init__(self,name)
        self.idNum = MITPerson.nextIDNum
        MITPerson.nextIDNum += 1
    
    def getIDnum(self):
        return self.idNum
    
    def __lt__(self,other):
        return self.idNum < other.idNum
    
    def speak(self,utterance):
        return (self.getLastName() + " says: " + utterance)
    

m3 = MITPerson('Mark Zuckerberg')
Person.setbirthday(m3,5,14,84)
m2 = MITPerson('Drew Houston')
Person.setbirthday(m2,3,4,83)
m1 = MITPerson('Bill Gates')
Person.setbirthday(m1,10,28,55)

m = [m1,m2,m3]
m.sort()
for element in m:
    print(element)
    

p1 = MITPerson('Eric')
p2 = MITPerson('John')
p3 = MITPerson('John')
p4 = Person('John')