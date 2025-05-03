#Excercise 1
class Circle():
    def __init__(self,radius):
        self.radius=radius

    def get_area(self):
        circle_area=self.radius*((3.14)**2)
        print(circle_area)
    
mycircle=Circle(1)
mycircle.get_area()

