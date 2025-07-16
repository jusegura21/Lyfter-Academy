import PySimpleGUI as sg
import persistency
import models
from constants import TEXT_ADD_CATEGORY_PROMPT,HEADERS,BTN_ADD_CATEGORY,BTN_ADD_EXPENSE,BTN_ADD_INCOME,TEXT_TITLE,FILENAME_CATEGORIES,FILENAME_TRANSACTIONS
# Declarar encabezados y datos
transactions = []  # debe ser lista de listas
category_list=[]
# Layout
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
    if event == BTN_ADD_CATEGORY:
        cat=sg.popup_get_text(TEXT_ADD_CATEGORY_PROMPT)
        category.categories.append(cat)
        print(category.categories)

    if event == BTN_ADD_INCOME:
        cat = category.choose_category()
        t=models.Transactions('Income')
        try:
            t.create_transaction(cat)
            transactions.append(t.transaction_to_list())
            window['-TABLE-'].update(values=transactions)
        except ValueError as e:
            sg.popup_error(str(e))

    if event == BTN_ADD_EXPENSE:
        cat= category.choose_category()
        t=models.Transactions('Expense')
        try:
            t.create_transaction(cat)
            transactions.append(t.transaction_to_list())
            window['-TABLE-'].update(values=transactions)
        except ValueError as e:
            sg.popup_error(str(e))                 

window.close()