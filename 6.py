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
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabbit: " + str(self.name) + " " + str(self.age)
    
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
            
    