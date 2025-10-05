import csv
import PySimpleGUI as sg
import os
from constants import TEXT_ADD_AMOUNT,TEXT_ADD_CATEGORY_PROMPT, TEXT_CHOOSE_CATEGORY, TEXT_CATEGORY_WARNING,POPUP_ERROR_EMPTY_DESC,POPUP_ERROR_INVALID_AMOUNT,POPUP_ERROR_AMOUNT_TOO_LOW,TEXT_ADD_DESCRIPTION
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
        new_category = sg.popup_get_text(TEXT_ADD_CATEGORY_PROMPT)
        return self.try_add_category(new_category)

            
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
                raise ValueError(POPUP_ERROR_EMPTY_DESC)
            try:
                amount=float(amount_text)
            except ValueError:
                raise ValueError(POPUP_ERROR_INVALID_AMOUNT)
            
            if amount <=0:
                    raise ValueError(POPUP_ERROR_AMOUNT_TOO_LOW)
            
            return description.strip(),amount       
        
    def create_transaction(self,category,desc,amount_text):
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