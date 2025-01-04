import flet as ft
from db_csv.expense import Expense

class ExpenseRow(ft.DataRow):
    def __init__(self, expense: Expense):
        super().__init__(
            cells=[
                ft.DataCell(ft.Text(expense.date)),
                ft.DataCell(ft.Text(expense.name)),
                ft.DataCell(ft.Text(expense.amount)),
            ]
        )