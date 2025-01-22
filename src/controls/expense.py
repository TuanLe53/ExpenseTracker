import flet as ft
from typing import List
from db.db import ExpenseModel

class Expenses(ft.Container):
    def __init__(self, page: ft.Page, expense_budget: int, expenses: List[ExpenseModel]):
        super().__init__()
        
        self.page = page
        
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
        
        content = ft.Column([
            ft.Row([
                ft.Text("Expenses"),
                ft.TextButton(
                        text="Details",
                        on_click=lambda e: self.page.go("/plan/expenses")
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.Text(f"{self.expense_budget:,}"),
            chart,
        ])
        
        self.content = content