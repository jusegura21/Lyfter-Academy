def parameter_print(func):
    def wrapper(*args,**kwargs):#
        for index,arg in enumerate(args):
            print(f'Arg{index}: {arg}')
        for index, kwarg in enumerate(kwargs):
            print(f'Arg{index}: {kwarg}')
        print('Parameters printed. Now the function will be executed')
        func(*args,**kwargs)
    return wrapper

def parameter_number_check(func):
    def wrapper(*args,**kwargs):
        count=0
        for index in args:
            if isinstance(index,(int,float)) and not isinstance(index,bool):
                pass
            else:
                count+=1
        for key, value in kwargs.items():
            if isinstance(value,(int,float)) and not isinstance(value,bool):
                pass
            else:
                count+=1
        if count>0:
            print(f'Error. "{count}" parameters of the function are not numbers.Function was not executed')
        else:
            print(f'Check succesfull. All parameters are numbers. Executing function...')
            func(*args,**kwargs)
    return wrapper  

@parameter_print
@parameter_number_check
def sumatory(*args,): #Function created to test parameter_print decorator. 
    total=0;
    for index, arg in enumerate(args):
        total+=arg
    print(f'the total is{total}')

sumatory(1,2,3,'q5')

