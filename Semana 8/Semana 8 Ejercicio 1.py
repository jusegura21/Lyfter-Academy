#Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro 
#archivo los mismos nombres ordenados alfabéticamente.

def index_swap(list,index): #Function that swap index n with n+1. 
    storage=list[index+1]
    list[index+1]=list[index]
    list[index]=storage
    return list
    
def open_and_create_list(path): #function that creates a list from reading the file
    list=[]
    with open(path, 'r',encoding='utf-8') as file:
        for line in file.readlines():
            list.append(line)
    return list

def sorter(list): #function that iterates the list and swaps index when needed.
    sorted_words=list
    storage=""
    contador=0
    for n in range(len(list)-1):
        if sorted_words[n][0]<=sorted_words[n+1][0]:
            contador+=1
            continue
        else:
            sorted_words=index_swap(sorted_words,n)
    return sorted_words, contador

def sec_sorter(list): #function that iterates the list looking for the second letter when the first letter is the same. 
    sorted_words=list
    storage=""
    contador2=0
    for n in range(len(list)-1):
        if sorted_words[n][0]==sorted_words[n+1][0]:
            if sorted_words[n][1]<=sorted_words[n+1][1]:
                continue
            else:
                sorted_words=index_swap(sorted_words,n)
                contador2+=1
    return sorted_words, contador2
        
def write_list_into_file(list,path): #function that writes the sorted list into a file
    with open(path,'a',encoding='utf-8') as file:
        for index in range(len(list)):
            file.write(list[index]) 
    return True

def main():
    new_list=open_and_create_list('lista de canciones.txt')
    while True: #funcion que llama a "sorter" N veces hasta que la lista se encuentre acomodada. 
        if sorter(new_list)[1]==len(new_list)-1:
            break
        else:
            new_list=sorter(new_list)[0]
    while True:
        if sec_sorter(new_list)[1]==0:
            break
        else:
            new_list=sec_sorter(new_list)[0]
    write_list_into_file(new_list,'myfile.txt')
    print('New file has been succesufully created.')


import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) #defining the path of the current folder
main()
