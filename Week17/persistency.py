import csv 
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def write_csv_file(file_path,data,headers):
    with open(file_path,'w',newline='',encoding='utf-8') as file:
        writer=csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

def read_csv_file(file_path,data,headers):
    if not os.path.isfile(file_path):
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()

    with open (file_path,newline='',encoding='utf-8') as file:
        if file.readable() and os.path.getsize(file_path)>0:
            file.seek(0)       
            reader = csv.DictReader(file)
            for line in reader:
                try:
                    data.append([line[headers[0]],line[headers[1]],line[headers[2]],float(line[headers[3]])])
                except KeyError:
                    pass

def write_category_list(list,path): #function that writes the list into a file
    with open(path,'w',encoding='utf-8') as file:
        for item in list:
            file.write(item+'\n') 
    return True

def read_list_from_file(path):
    if not os.path.isfile(path):
        return []  # si no existe, devolvés una lista vacía
    with open(path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]