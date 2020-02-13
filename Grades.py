class student(object):
    nextIdNum = 0
    def __init__(self,name):
        self.name = name
        self.lastName = name[-1]
        self.idNum = nextIdNum
        student.nextIdNum += 1
    
    def getIDNum(self):
        return self.idNum

###
####
#### New classes below


class Grades(object):
    def __init__(self):
        """Create and empty grade book"""
        self.students = [] #list of student objects
        self.grades = {} #maps idnum -> list of grades
        self.isSorted = True  #true if self.students is sorted
        
    def addstudent(self,student):
        '''Assumes student is of type student
            add student to the grade book'''
        
        if student in self.students:
            raise ValueError('Duplicate statement')
        
        self.students.append(student)
        self.grades[student.getIDNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        '''Assumes: grade is a float
            Add grade to the list of grades for student'''
        try:
            self.grades[student.getIDNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')
        
    def getGrades(self,student):
        '''Return a list of grades for students'''
        try: #return a copy of student grades
            return self.grades[student.getIDNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')