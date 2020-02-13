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
 
class student(MITPerson):
    pass 
    
class UG(student):
    def __init__(self,name,classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    
    def getClass(self):
        return self.year
    
    def speak(self, utterance):
        return MITPerson.speak(self, " Dude, " + utterance)

class Grad(student):
    pass

class TransferStudents(student):
    pass

def isStudent(obj):
    return isinstance(obj, student)


#
#
#
# Professor class is initialized here

class Professor(MITPerson):
    def __init__(self,name,department):
        MITPerson.__init__(self,name)
        self.department = department
    
    def speak(self, utterance):
        new = 'In course' + self.department + 'we say'
        return MITPerson.speak(self, new + utterance)
    
    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)