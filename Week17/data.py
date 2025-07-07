class Expense(): 
    def __init__(self,category, description, amount):
        self.category=category
        self.description=description
        self.amount=amount

    def create_expense(self):
        expense=['Expense']
        expense.append(self.category)
        expense.append(self.description)
        expense.append(self.amount)
        return expense

class Income():
    def __init__(self,category,description,amount):
        self.category=category
        self.description=description
        self.amount=amount
    def create_income(self):
        income=['Income']
        income.append(self.category)
        income.append(self.description)
        income.append(self.amount)
        return income

