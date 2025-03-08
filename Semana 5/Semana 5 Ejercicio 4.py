my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
booleano=True
while booleano:
    for n in range(len(my_list)):
        if (my_list[n]%2 != 0):
            my_list.pop(n)
            booleano=True
            break   
        else:
            booleano=False 
print(my_list)