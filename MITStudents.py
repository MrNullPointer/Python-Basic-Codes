import datetime

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
        return "The persons name is: " + self.name 
    
      
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
    
class UG(MITPerson):
    def __init__(self,name,classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    
    def getClass(self):
        return self.year
    
    def speak(self, utterance):
        return MITPerson.speak(self, " Dude, " + utterance)

class Grad(MITPerson):
    pass

def isStudent(obj):
    return isinstance(obj, UG) or isinstance(obj, Grad)