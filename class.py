
'''
class A:
   x=10
   y=20
   def add(self,a,b):
   	print('i am a keyword')
   	return a+b
   def mul(self,x,y):
   	return self.x*self.y
a=A()
print(a.add(10,30))   	
print(a.mul(40,50))
'''
'''
class Prasad:
	def __init__(self):
	    print('in am a constructor')
	def add(self,a,b):
	    return a+b

p=Prasad()
print(p.add(10,40))	        
'''
class Prasad:
	def __init__(self,x,y):
	    self.x=x
	    self.y=y
	def add(self,a,b):
	    print(a+b)
	    return self.x+self.y
	def mult(self):
	    return self.x * self.y

p=Prasad(10,30)
print(p.add(40,50))	    

	    	







