# Python example to show that base
# class members can be accessed in
# derived class using super()
class Base(object):

	# Constructor
	def __init__(self, x):
		self.x = 30

class Derived(Base):

	# Constructor
	def __init__(self, x, y):
		
		''' In Python 3.x, "super().__init__(name)"
			also works'''
		#super(Derived, self).__init__(x)
		self.x=x
		self.y = y

	def printXY(self):

	# Note that Base.x won't work here
	# because super() is used in constructor
	    print(Base.x, self.y)


# Driver Code
d = Derived(10, 20)
d.printXY()
