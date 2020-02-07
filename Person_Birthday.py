import datetime

class Person(object):
    def __init__(self,name):
        '''This function only requires a name'''
        self.name = name
        self.birthday = None
        self.lastname = name.split()[-1]
        
    def setbirthday(self,month,day,year):
        '''This function requires birthday for a person'''
        self.birthday = datetime.date(year,month,day)
        
    def age(self):
        '''This function gives the current age of person'''
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days