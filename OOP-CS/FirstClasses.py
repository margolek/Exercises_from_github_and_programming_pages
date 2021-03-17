
class Employee:
	#Create __init__ method to create atributes
	def __init__(self,first,last,email):
		self.first = first
		self.last = last
		self.email = email

	#Always put instance as function argument
	def merge(self):
		fulname = self.first + ' ' + self.last
		return fulname



#Creating class instance
emp_1 = Employee('Slavko','Smith','ssmith@gmail.com')
print(emp_1.merge())