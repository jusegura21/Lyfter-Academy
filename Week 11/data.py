import csv
import os

def export_file(file_path, data, headers):
    with open(file_path, 'w', newline='' ,encoding='utf-8') as file:
        writer = csv.DictWriter(file,fieldnames= headers)
        writer.writeheader()
        writer.writerows(data)

def import_file(file_path):
    data=[]
    try:
        with open(file_path,'r',newline='',encoding='utf-8') as file:
            csv_reader=csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        return data # Read all rows into a list of dictionaries
    except FileNotFoundError as e:
        print(f'File not found:{e}')

def print_current_student_list(list):
    print(list)

def show_top_3(student_list):
    sorted_list = sorted(student_list, key=lambda Student: Student.average_score,reverse=True)
    counter=0
    print('---Top 3 Students---')
    while counter<3:
        print(sorted_list[counter].name, sorted_list[counter].average_score)
        counter+=1