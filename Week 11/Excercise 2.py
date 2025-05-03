#Excercise 2
class Person():
    def __init__(self,name):
        self.name=name
        print(f'{name} has born!')
    
class Buss():
    def __init__(self):
        self.max_passengers=50
        self.current_passengers=0
        self.passenger_list=[]
    
    def add_passengers(self,passenger):
        if self.current_passengers<self.max_passengers:
            self.current_passengers+=1
            self.passenger_list.append(passenger)

        else:
            print("Bus is full!")

    def remove_passenger(self,name):
        cont=0
        for n in self.passenger_list:
            cont+=1
            if name==n.name:
                self.passenger_list.pop(cont-1)

person1=Person('Julian')
person2=Person('Jenifer')                           
Mybuss=Buss()
Mybuss.add_passengers(person1)
Mybuss.add_passengers(person2)
print(Mybuss.passenger_list[0].name, Mybuss.passenger_list[1].name)
Mybuss.remove_passenger('Julian')
print(Mybuss.passenger_list)