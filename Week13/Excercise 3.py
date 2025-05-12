from datetime import date
class Person():
    def __init__(self, name):
        self.name = name

class User():
    date_of_birth: date
    def __init__(self,person,date_of_birth):
        self.date_of_birth=date_of_birth
        self.person=person

    @property
    def age(self):
        today = date.today()
        return (today.year- self.date_of_birth.year- ((today.month, today.day)< (self.date_of_birth.month, self.date_of_birth.day)))
    
    @classmethod
    def legal_age(cls,name,date_of_birth):
        person=Person(name)
        user=User(person,date_of_birth)
        if user.age>18:
            print("Legal of age verified.")
            return user
        else: 
            return print(f'Not legal of age: {user.age} years old')
        
print(User.legal_age('Fulanito',date(2001,1,1)).date_of_birth)


