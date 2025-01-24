import flet as ft
from db_csv.expense import Expense
from .expense import ExpenseRow

class ExpenseList(ft.DataTable):
    def __init__(self, expenses: list[Expense]):
        columns = [
            ft.DataColumn(ft.Text("Date")),
            ft.DataColumn(ft.Text("Name")),
            ft.DataColumn(ft.Text("Amount")),
            ft.DataColumn(ft.Text("Delete")),
        ]
        super().__init__(columns)
        
        
        self.rows = [ExpenseRow(expense, self) for expense in expenses]