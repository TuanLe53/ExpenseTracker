import flet as ft
from controls.expense_list import ExpenseList
from db.expense import get_expenses_from_current_plan

class ExpensesView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.page = page
        
        self.expenses = []
        self.controls = []
        
    def did_mount(self):
        self.expenses = get_expenses_from_current_plan()
        self.controls = [ExpenseList(self.expenses)]
        self.update()