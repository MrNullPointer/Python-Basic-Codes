#class basic

class coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def difference(self,other):
        xdiff = (self.x - other.x)**2
        ydiff = (self.y - other.y)**2
        return (xdiff + ydiff)**0.5
    
    def __str__(self):
        return "<" + str(self.x) + ',' + str(self.y) + ">"
    def __sub__(self,other):
        return coordinate(self.x - other.x, self.y - other.y)