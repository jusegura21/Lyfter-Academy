import PySimpleGUI as sg
import persistency
import models
from constants import TEXT_CATEGORY_WARNING,TEXT_ADD_DESCRIPTION,TEXT_ADD_AMOUNT,TEXT_CHOOSE_CATEGORY,TEXT_ADD_CATEGORY_PROMPT,HEADERS,BTN_ADD_CATEGORY,BTN_ADD_EXPENSE,BTN_ADD_INCOME,TEXT_TITLE,FILENAME_CATEGORIES,FILENAME_TRANSACTIONS
# Declarar encabezados y datos
transactions = []  # debe ser lista de listas
category_list=[]
# Layout 1
layout = [
    [sg.Text(TEXT_TITLE)],
    [sg.Table(
        values=transactions,
        headings=HEADERS,
        auto_size_columns=True,
        justification='left',
        num_rows=5,
        key='-TABLE-'
    )],
    [sg.Button(BTN_ADD_EXPENSE)],
    [sg.Button(BTN_ADD_INCOME)],
    [sg.Button(BTN_ADD_CATEGORY)]
]

# Crear ventana
category=models.Categories(FILENAME_CATEGORIES,category_list)
category.read_list_from_file()
persist=persistency.Persistency(FILENAME_TRANSACTIONS,transactions,HEADERS)
persist.read_csv_file()
window = sg.Window("Main Window", layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        print("Guardando en archivo:", transactions)
        persist.write_csv_file()
        category.write_category_list()
        break
# === Create new category ===
    if event == BTN_ADD_CATEGORY:
        cat=sg.popup_get_text(TEXT_ADD_CATEGORY_PROMPT)
        if cat and cat.strip():    
            category.categories.append(cat)
            print(category.categories)
# === Add income or expense ===
    if event == BTN_ADD_INCOME or event == BTN_ADD_EXPENSE:
        if event == BTN_ADD_INCOME:
            t=models.Transactions('Income')
        elif event==BTN_ADD_EXPENSE:
            t=models.Transactions('Expense')
#layout for choosing catergories       
        layout2 = [
    [sg.Text(TEXT_CHOOSE_CATEGORY)],
    [sg.Combo(category.categories, key='-CATEGORIA-', readonly=True)],
    [sg.Button('OK'), sg.Button('Cancel')]
]
        win = sg.Window("Category", layout2, modal=True)
        while True:
            event, values = win.read()
            if event in (sg.WIN_CLOSED, 'Cancel'):
                selected=None 
                break
            if event == 'OK':
                selected=values['-CATEGORIA-']
                if not selected:
                    sg.popup_error(TEXT_CATEGORY_WARNING)
                    continue
                break
        win.close()              
        if selected is None:
            continue
        else:    
            desc=sg.popup_get_text(TEXT_ADD_DESCRIPTION)
            amount_text=sg.popup_get_text(TEXT_ADD_AMOUNT)
            t.create_transaction(selected,desc,amount_text)
            transactions.append(t.transaction_to_list())
            window['-TABLE-'].update(values=transactions)                

window.close()