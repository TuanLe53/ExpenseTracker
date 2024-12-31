import flet as ft
import datetime

class Expense(ft.Column):
    def __init__(self, page):
        super().__init__()
        
        self.expense_name = ft.TextField(hint_text="Enter your expense name", width=300)
        self.expense_amount = ft.TextField(hint_text="Enter your expense amount", width=300)
        self.expense_date = ""
        self.expense_date_btn = ft.ElevatedButton(
            "Select Date",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(
                ft.DatePicker(
                    first_date=datetime.datetime(year=2023, month=10, day=1),
                    last_date=datetime.datetime.now(),
                    on_change=self.on_date_change,
                    # on_dismiss=handle_dismissal,
                )
            )
        )
        self.expense_category = ft.Dropdown(
            width=300,
            options=[
                ft.dropdown.Option("Food"),
                ft.dropdown.Option("Transportation"),
                ft.dropdown.Option("Health"),
                ft.dropdown.Option("Entertainment"),
                ft.dropdown.Option("Education"),
                ft.dropdown.Option("Others"),
            ]
        )
        self.result = ft.Text("")
        
        self.controls=[
            ft.Column([ft.Text("Expense Name"), self.expense_name]),
            ft.Column([ft.Text("Expense Amount"), self.expense_amount]),
            ft.Row([ft.Text("Expense Date"), self.expense_date_btn]),
            ft.Column([ft.Text("Category"), self.expense_category]),
            self.result,
            ft.ElevatedButton("Add Expense", on_click=self.on_click),
        ]
        
    def on_date_change(self, e):
        self.expense_date = e.control.value.strftime("%d/%m/%Y")
    
    def on_click(self, e):
        name = self.expense_name.value
        amount = self.expense_amount.value
        date = self.expense_date
        category = self.expense_category.value
        self.result.value = f"Name: {name}, Amount: {amount}, Date: {date}, Category: {category}"
        self.update()