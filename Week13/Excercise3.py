from datetime import date

def legal_age(func):
    def wrapper(user,*args):
        age=user.age
        if age>18:
            print("Legal of age verified.")
            func(user,*args)
        else: 
            print(f'Not legal of age: {user.name}is {user.age} years old')
    return wrapper         
        
class User():
    date_of_birth: date
    def __init__(self,name,date_of_birth):
        self.name=name
        self.date_of_birth=date_of_birth

    @property
    def age(self):
        today = date.today()
        return (today.year- self.date_of_birth.year- ((today.month, today.day)< (self.date_of_birth.month, self.date_of_birth.day)))
    
@legal_age
def bar_entry(user,queue):
    queue.append(user)
    print(f'{user.name} got in!')
    
queue=[]
Person1=User('Julian', date(1996,3,21))
bar_entry(Person1,queue)
Person2=User('Dirk', date(2000,3,21))
bar_entry(Person2, queue)
Person3=User('Michi',date(2014,6,12))
bar_entry(Person3,queue)
print(queue)
