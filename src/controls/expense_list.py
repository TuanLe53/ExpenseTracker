import uuid
import flet as ft
from db_csv.expense import Expense, delete_expense_by_id
from .expense_row import ExpenseRow

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
        
class ExpenseRow(ft.DataRow):
    def __init__(self, expense: Expense, parent):
        self.parent = parent
        super().__init__(
            cells=[
                ft.DataCell(ft.Text(expense.date)),
                ft.DataCell(ft.Text(expense.name)),
                ft.DataCell(ft.Text(expense.amount)),
                ft.DataCell(ft.IconButton(
                    icon=ft.Icons.DELETE_FOREVER_ROUNDED,
                    icon_color="red500",
                    icon_size=40,
                    tooltip="Delete expense",
                    on_click=lambda e: self.delete(e, expense.id)
                ))
            ]
        )
        
    def delete(self, e, expense_id: uuid.UUID) -> None:
        delete_expense_by_id(expense_id)
        self.parent.rows.remove(self)
        self.parent.update()