import datetime

class Person(object):
    def __init__(self, name):
        '''Create a person called name'''
        self.name = name
        self.birthday = None
        self.lastName = name.split()[-1]

    def getLastName(self):
        '''return the last name of person'''
        return self.lastName

    def setBirthday(self,month,day,year):
        '''set self's birthday to birthDate'''
        self.birthday = datetime.date(year,month,day)

    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self,other):
        '''Returns the lesser value'''
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        '''return self's name'''
        return self.name

class MITPerson(Person):
    nextIdnum = 0  #next ID num to assign

    def __init__(self,name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdnum
        MITPerson.nextIdnum += 1

    def getIDNum(self):
        return self.idNum

    def __lt__(self,other):
        return self.idNum < other.idNum

    def speak(self,utterance):
        return (self.getLastName() + " says: " + utterance)

class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self,name,classYear):
        MITPerson.__init__(self,name)  #this will be passed to further person method
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self,utterance):
        return MITPerson.speak(self, " Dude, " + utterance)

class Grad(Student):
    pass

class TransferStudent(Student):
    pass

class Professor(MITPerson):
    def __init__(self,name,department):
        MITPerson.__init__(self,name)
        self.department = department

    def speak(self,utterance):
        new = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self, new + utterance)

    def lecture(self,topic):
        return self.speak(' it is obvious that ' + topic)

def isStudent(obj):
    return isinstance(obj,Student)


# Creating some Undergrads and Grads
s1 = UG('Matt Damon',2017)
s2 = UG('Ben Affleck',2017)
s3 = UG('Lin Manuel Miranda',2018)
s4 = Grad('Leonardo di Caprio')

Faculty = Professor('Doctor Arrogant', 'Six')

m3 = MITPerson('Mark Zuckerberg')
Person.setBirthday(m3,5,14,84)
m2 = MITPerson('Drew Houston')
Person.setBirthday(m2,3,4,83)
m1 = MITPerson('Bill Gates')
Person.setBirthday(m1,10,28,55)
#
# MITPersonList = [m1,m2,m3]
#
# for element in MITPersonList:
#     print (element)
#
# MITPersonList.sort()
#
# for elem in MITPersonList:
#     print(elem)

p1 = MITPerson('Eric')
p2 = MITPerson('John')
p3 = MITPerson('John')
p4 = Person('John')