import csv
import os


def write_csv_file(file_path,data,headers):
    with open(file_path,'w',encoding='utf-8') as file:
        writer=csv.DictWriter(file,headers)
        writer.writeheader()
        writer.writerows(data)
def create_dictionary(list1,listb):
    cont=0
    dictionary={}
    for index in list1:
        dictionary[index]=listb[cont]
        cont+=1
    return dictionary
        
        

def main():
    dictionary_list=[]
    while True:
        data_list=[]
        data_list.append(input('Please enter the movie name: '))
        data_list.append(input('Please enter the movie gender: '))
        data_list.append(input('Please enter the movie developers: '))
        data_list.append(input('Please enter the ESRB category: '))
        dictionary_list.append(create_dictionary(keys,data_list))
        while True:
            try: 
                a=int(input("Press 1 and enter to add another movie, or ay other key to continue."))
                break
            except ValueError as error:
                print(f"No ha ingresado un numero valido:{error}") 
        if a!=1:
            break
    return dictionary_list
    

os.chdir(os.path.dirname(os.path.abspath(__file__))) #defining the path of the current folder
keys=['name', 'gender','developer','category']
dictionary_list=main()
write_csv_file('movies.csv',dictionary_list,keys)