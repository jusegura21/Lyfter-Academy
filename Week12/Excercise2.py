from abc import ABC, abstractmethod


class shape(ABC):
	@abstractmethod
	def calculate_perimeter(self):
		pass
	def calculate_area(self):
		pass

class Square(shape):
	def __init__(self,side):
		self.side=side
		
	def calculate_perimeter(self):
		perimeter=self.side*4
		print("The perimeter is",perimeter)
		
	def calculate_area(self):
		area=self.side*self.side
		print("The area is",area)
		

class Circle(shape):
	def __init__(self,radius):
		self.radius=radius

	def calculate_perimeter(self):
		perimeter=2*3.14*self.radius
		print(f"The perimeter is {perimeter}. ")
		
	def calculate_area(self):
		area=3.14*self.radius*self.radius
		print(f"The area is {area}. ")
        
class Rectangle(shape):
	def __init__(self,long_side,short_side):
		self.long_side=long_side
		self.short_side=short_side
		
	def calculate_perimeter(self):
		perimeter=self.long_side+self.long_side+self.short_side+self.short_side
		print(f"The perimeter is {perimeter}. ")
		
	def calculate_area(self):
		area=self.long_side*self.short_side
		print(f"The area is {area}. ")

Mycircle=Circle(3)
Mycircle.calculate_area()
Mycircle.calculate_perimeter()
Myrectangle=Rectangle(2,3)
Myrectangle.calculate_area()
Myrectangle.calculate_perimeter()
Mysquare=Square(5)
Mysquare.calculate_area()
Mysquare.calculate_perimeter()
