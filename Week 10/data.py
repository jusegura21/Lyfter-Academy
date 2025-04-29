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

def show_top_3(dictionaries_list):
    counter=0
    sorted_dict = sorted(dictionaries_list, key=lambda x: float(x['average_score']),reverse=True)
    for row in sorted_dict:
                print ( f'Student:{row['name']} Avg Score: {row['average_score']}')
                counter+=1
                if counter==3:
                    break
        