class Employee:

	num_of_emps = 0
	raise_amount = 1.04

	#Create __init__ method to create atributes
	def __init__(self,first,last,email,pay):
		self.first = first
		self.last = last
		self.email = email
		self.pay = pay

		Employee.num_of_emps +=1

	#Always put instance as function argument
	def merge(self):
		fulname = self.first + ' ' + self.last
		return fulname

	def apply_raise(self):
		pay = self.pay * self.raise_amount
		return pay



#Creating class instance
emp_1 = Employee('Slavko','Smith','ssmith@gmail.com',1000)
emp_2 = Employee('Marko','Polo','mpolo@gmail.com',5000)

#Change class variable value for specific instance
emp_2.raise_amount = 1.05
print(emp_2.raise_amount)
print(emp_1.apply_raise())
print(Employee.num_of_emps)