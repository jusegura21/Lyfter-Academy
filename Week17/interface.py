import PySimpleGUI as sg
import data
import persistency

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
def choose_category():
    layout = [
        [sg.Text('Choose category:')],
        [sg.Combo(category_list, key='-CATEGORIA-',  readonly=True)],
        [sg.Button('OK'), sg.Button('Cancel')]
    ]
    win = sg.Window("Category", layout, modal=True)
    while True:
        event, values = win.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            win.close()
            return None
        if event == 'OK':
            win.close()
            return values['-CATEGORIA-']
# Crear ventana
category_list=persistency.read_list_from_file('categories.txt')
persistency.read_csv_file('transactions.csv',transactions,headers)
window = sg.Window("Main Window", layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        print("Guardando en archivo:", transactions)
        persistency.write_csv_file('transactions.csv',transactions,headers)
        persistency.write_category_list(category_list,'categories.txt')
        break
    if event == 'Add Category':
        category=sg.popup_get_text('Add the category name')
        category_list.append(category)

    if event == 'Add Income':
        category = choose_category()
        description = sg.popup_get_text('Add Income Description')
        try:
            amount=sg.popup_get_text('Add Amount')
            amount= float(amount) #Duda con los values
        except ValueError:
            sg.popup("Please enter a valid number")
        income= data.Income(category,description,amount)
        transactions.append(income.create_income())
        window['-TABLE-'].update(values=transactions)

    if event == 'Add Expense':
        category = choose_category()
        description = sg.popup_get_text('Add Expense Description')
        try:
            amount=sg.popup_get_text('Add Amount')
            amount=(-1)*float(amount) #Duda con los values
        except ValueError:
            sg.popup("Please enter a valid number")
        
        expense = data.Expense(category,description,amount)
        transactions.append(expense.create_expense())
        window['-TABLE-'].update(values=transactions)                  

window.close()