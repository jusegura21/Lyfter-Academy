import csv
import os

def export_file(file_path, data, headers):
    # Check if the file exists and is not empty
    #file_exists = os.path.isfile(file_path) and os.path.getsize(file_path) > 0
    with open(file_path, 'w', newline='' ,encoding='utf-8') as file:
        writer = csv.DictWriter(file,fieldnames= headers)
        #if not file_exists:
            #writer.writeheaders()  # Write the headers first (only once)
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

def show_all_data(file_path):
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            csv_reader=csv.reader(file)
            for row in csv_reader:
                print(row)
    except FileNotFoundError as e:
        print(f'Error:{e}')

def show_top_3(file_path,sort_key):
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            counter=0
            csv_reader=csv.DictReader(file)
            sorted_file=sorted(csv_reader,key=lambda x: float(x[sort_key]),reverse=True)
            for row in sorted_file:
                print ( f'Student:{row['name']} Avg Score: {row['average_score']}')
                counter+=1
                if counter==3:
                    break
    except FileNotFoundError as e:
        print(f'Error:{e}')

def show_all_avg_score(file_path,sort_key):
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            csv_reader=csv.reader(file)
            for row in csv_reader:
                print(row[0],'Avg Score:',row[6])
    except FileNotFoundError as e:
        print(f'Error:{e}')