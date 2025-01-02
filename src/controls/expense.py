import flet as ft
from db_csv.expense import Expense

class ExpenseRow(ft.Row):
    def __init__(self, expense: Expense):
        super().__init__()
        
        self.date = ft.Text(expense.date, width=300)
        self.name = ft.Text(expense.name, width=300)
        self.amount = ft.Text(expense.amount, width=300)
        
        self.controls = [
            self.date,
            self.name,
            self.amount,
        ]