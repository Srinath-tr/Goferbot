class person:
    def __init__(self,name):
        self.name = name
        
    def printname(self):
        return self.name

    def isemployee(self):
        return False

class employee(person):
    def isemployee(self):
        return True
    def gos(self):

emp = employee('Srinath')
print(emp.printname(),emp.isemployee())

per = person('Gos')
print(per.printname(),per.isemployee())
