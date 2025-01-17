import flet as ft
from typing import List
from controls.expense_list import ExpenseList
from db.db import ExpenseModel


class Expenses(ft.Column):
    def __init__(self, expense_budget: int, expenses: List[ExpenseModel]):
        super().__init__()
        
        self.expense_budget = expense_budget
        self.expenses = expenses
        
        self.total_expense = sum(expense.amount for expense in self.expenses)

        self.expense_percentage = self.total_expense / self.expense_budget * 100
        self.remain_percentage = 100 - self.expense_percentage
                
        chart = ft.PieChart(
            sections=[
                ft.PieChartSection(
                self.expense_percentage,
                title=f"{self.expense_percentage}%",
                color=ft.Colors.BLUE,
            ),
                ft.PieChartSection(
                self.remain_percentage,
                title=f"{self.remain_percentage}%",
                color=ft.Colors.GREEN,
            ),
            ],
            sections_space=0,
            center_space_radius=40,
            expand=True,
        )
        
        self.controls = [
            ft.Text("Expenses"),
            ft.Text(f"{self.expense_budget:,}"),
            chart,
            ExpenseList(self.expenses)
        ]