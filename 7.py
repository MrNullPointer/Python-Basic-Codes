import numpy as np

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
    
class Person(Animal):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friends(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("Hello!")
    def age_diff(self,other):
        return self.get_age() - other.get_age()
    def __str__(self):
        return "Person: " + str(self.name) + " : " + str(self.age)
            
class Student(Person):
    def __init__(self,name,age,major = None):
        Person.__init__(self,name,age)
        self.major = major
    def change_major(self, major):
        self.major = major
    def speak(self):
        r = np.random.random()
        if r < 0.25:
            print("I have homework!") 
        elif 0.25 <= r < 0.5:
            print("I need sleep!")
        elif 0.5 <= r < 0.75:
            print("I should eat!!")
        else:
            print("I am watching TV!")
    def __str__(self):
        return "Student: " + str(self.name) + ' ' + str(self.age) + ' ' + str(self.major)   