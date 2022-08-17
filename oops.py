#oops: oops stands for object oriented programing structure, which is used to hold a python objects.
'''
oops comes with two major concepts:
1. class 
2. object

by using oops we can provide security, extendability, resusability
we can create class by using class key word
class:
it is container which is used to hold a python properties.
object:
it is intance of the class or blue print of class.
'''
class Prasad:
	x = 10
	y = 20

prasad = Prasad()

#get
#print(prasad.x)
#print(prasad.y)

#update
prasad.x = 30
#print(prasad.x)

#new variable

prasad.z = 15

#print(prasad.z)

#delete
del prasad.z
#print(prasad.z)
'''
'''
'''
p = Prasad()

print(p.x)
p.x = 50
print(p.x)

obj = prasad

print(obj.x)
'''
'''
class A:
	x = 10
	y = 20
	def add(self, a, b):
		return a * b
a = A()
print(a.add(10, 5))
'''
'''
class A:
	x = 10
	y = 20
	def add(self, a, b):
		return self.x + self.y
a = A()
print(a.add(1, 2))
'''
'''
class A:
	x = 10
	y = 20
	def add(self, a, b):
		return self.x + self.y
class B:
	def add(self, a, b):
		return a * b

a = A()
print(a.add(1, 2))
b = B()
print(b.add(20, 5))
'''
'''
class Employee:
	id_ = 100
	name = 'prasad'
	company = 'tcs'
	salary = 30000

emp1 = Employee()
emp1.salary = 35000
emp2 = emp1
emp3 = Employee()
print(emp2.salary) #35000
print(emp1.salary) #35000
print(emp3.salary) #30000
'''
'''
l = ['hello', 'my', 'name', 'is', 'prasad']
#output = 3 (how many 'a' s in the given data structure)

print({i:(i.count('a')) for i in l})
print({i:len(i) for i in l})

'''
'''
l=['hi','hello','fine']
print({i:(i.count('l')) for i in l})
'''

#s='hello','python','world'
#print({i:len(i) for i in s})
k='hello python world'
#print({i:(i.count('h')) for i in k})
#print({i:(k.count('e')) for i in k})
print({i:len(i) for i in k.split()})

print({i:k.count(i) for i in k})











