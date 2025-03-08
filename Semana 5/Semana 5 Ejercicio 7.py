list_a=['brand','series','model','hp']
list_b=['Audi','Q5','2014','220']
cont = 0
dictionary ={}
for index in list_a:
    dictionary[index] = list_b[cont]
    cont+=1
print(dictionary)