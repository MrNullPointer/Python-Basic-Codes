# Integer set class

class intset(object):
    def __init__(self):
        self.num = []
    def insert(self,e):
        if e not in self.num:
            self.num.append(e)
    def member(self,e):
        return e in self.num
    def __str__(self):
        result = ''
        for i in self.num:
            result += str(i) + ','
        return result[:-1]
    def remove(self,e):
        try:
            self.num.remove(e)
        except:
            raise ValueError (str(e) + 'not found!!')