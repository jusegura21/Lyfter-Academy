import csv
import PySimpleGUI as sg
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Persistency():
    def __init__(self,path,data,headers):
        self.path=path
        self.data=data
        self.headers=headers

    def write_csv_file(self):
        with open(self.path,'w',newline='',encoding='utf-8') as file:
            writer=csv.writer(file)
            writer.writerow(self.headers)
            writer.writerows(self.data)
    
    def read_csv_file(self):
        if not os.path.isfile(self.path):
            with open(self.path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                writer.writeheader()

        with open (self.path,newline='',encoding='utf-8') as file:
            if file.readable() and os.path.getsize(self.path)>0:
                file.seek(0)       
                reader = csv.DictReader(file)
                for line in reader:
                    try:
                        self.data.append([line[self.headers[0]],line[self.headers[1]],line[self.headers[2]],float(line[self.headers[3]])])
                    except KeyError:
                        pass