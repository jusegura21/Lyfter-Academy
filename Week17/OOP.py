import csv
import PySimpleGUI as sg
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Categories():
    def __init__(self,path,categories):
        self.path=path
        self.categories=categories

    def try_add_category(self,new_category):
        if new_category:
            cleaned = new_category.strip()
            if cleaned and cleaned not in self.categories:
                self.categories.append(cleaned)
                return True
        return False

    def add_category(self):
        new_category = sg.popup_get_text('Add the category name')
        return self.try_add_category(new_category)

    def choose_category(self):
        layout = [
            [sg.Text('Choose category:')],
            [sg.Combo(self.categories, key='-CATEGORIA-',  readonly=True)],
            [sg.Button('OK'), sg.Button('Cancel')]
        ]
        win = sg.Window("Category", layout, modal=True)
        while True:
            event, values = win.read()
            if event in (sg.WIN_CLOSED, 'Cancel'):
                win.close()
                return None
            if event == 'OK':
                selected=values['-CATEGORIA-']
                if not selected:
                    sg.popup_error('Warning: Category Selection is recommended but you can continue')
                    win.close()
                    return None
                    #raise ValueError('Category selection is required')
                win.close()
                return selected
            
    def write_category_list(self): #function that writes the list into a file
        with open(self.path,'w',encoding='utf-8') as file:
            for item in self.categories:
                file.write(item+'\n') 
        return True
    
    def read_list_from_file(self):
        if not  os.path.isfile(self.path):
            self.categories=[]  # si no existe, devolvés una lista vacía
        with open(self.path, 'r', encoding='utf-8') as file:
            self.categories=[line.strip() for line in file if line.strip()]
        return self.categories


class Transactions():
    description=''
    amount=0
    category=''
    def __init__(self,type):   
        self.type=type

    def set_transaction_data(self,description,amount_text): 
            if not description or not description.strip():
                raise ValueError('Description cannot be empty')
            try:
                amount=float(amount_text)
            except ValueError:
                raise ValueError('Invalid amount format')
            
            if amount <=0:
                    raise ValueError('Amount must be greater than 0')
            
            return description.strip(),amount       
        
    def create_transaction(self,category):
        desc=sg.popup_get_text('Add Income Description')
        amount_text=sg.popup_get_text('Add Amount')

        desc_clean, amount = self.set_transaction_data(desc,amount_text)
        self.description=desc_clean
        self.category=category
        self.amount= -amount if self.type=='Expense' else amount
       



    def transaction_to_list(self):
        transaction_list=[]
        transaction_list.append(self.type)
        transaction_list.append(self.category)
        transaction_list.append(self.description)
        transaction_list.append(self.amount)
        return transaction_list

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