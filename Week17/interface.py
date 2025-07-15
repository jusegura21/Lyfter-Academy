import PySimpleGUI as sg
import OOP
# Declarar encabezados y datos
headers = [' Type ', 'Category', 'Description', 'Amount']
transactions = []  # debe ser lista de listas
category_list=[]
# Layout
layout = [
    [sg.Text('My Transactions')],
    [sg.Table(
        values=transactions,
        headings=headers,
        auto_size_columns=True,
        justification='left',
        num_rows=5,
        key='-TABLE-'
    )],
    [sg.Button('Add Expense')],
    [sg.Button('Add Income')],
    [sg.Button('Add Category')]
]
# Crear ventana
category=OOP.Categories('categories.txt',category_list)
category.read_list_from_file()
persist=OOP.Persistency('transactions.csv',transactions,headers)
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
    if event == 'Add Category':
        cat=sg.popup_get_text('Add the category name')
        category.categories.append(cat)
        print(category.categories)

    if event == 'Add Income':
        cat = category.choose_category()
        t=OOP.Transactions('Income')
        try:
            t.create_transaction(cat)
            transactions.append(t.transaction_to_list())
            window['-TABLE-'].update(values=transactions)
        except ValueError as e:
            sg.popup_error(str(e))

    if event == 'Add Expense':
        cat= category.choose_category()
        t=OOP.Transactions('Expense')
        try:
            t.create_transaction(cat)
            transactions.append(t.transaction_to_list())
            window['-TABLE-'].update(values=transactions)
        except ValueError as e:
            sg.popup_error(str(e))                 

window.close()