import flet as ft
from controls.navigation_bar import NavBar
import datetime
from db_csv.expense import Expense, add_expense_to_csv

class NewExpenseView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.page = page
        self.route = "/expense/new"
        self.navigation_bar = NavBar(self.page)
        
        self.expense_name = ft.TextField(hint_text="Enter your expense name", width=300)
        self.expense_amount = ft.TextField(hint_text="Enter your expense amount", width=300)
        
        self.expense_date = datetime.datetime.now().strftime("%d/%m/%Y")
        self.expense_date_helper_text = ft.Text("", visible=False)
        self.expense_date_btn = ft.ElevatedButton(
            "Select a date (leave it blank to use today's date)",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: self.page.open(
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
            ],
            on_change= self.on_category_change
        )
        self.other_category = ft.TextField(hint_text="Enter your category", width=300, visible=False)
        self.note = ft.TextField(hint_text="Enter your note", width=300)
        
        
        self.result = ft.Text("")
        
        self.controls=[
            ft.Column([ft.Text("Expense Name"), self.expense_name]),
            ft.Column([ft.Text("Expense Amount"), self.expense_amount]),
            ft.Row([ft.Text("Expense Date"), self.expense_date_helper_text, self.expense_date_btn]),
            ft.Column([ft.Text("Category"), self.expense_category]),
            self.other_category,
            ft.Column([ft.Text("Note"), self.note]),
            self.result,
            ft.ElevatedButton("Add Expense", on_click=self.on_click),
        ]
        
    def on_date_change(self, e):
        self.expense_date = e.control.value.strftime("%d/%m/%Y")
        
        self.expense_date_btn.text = "Change date"
        
        self.expense_date_helper_text.value = f"{self.expense_date}"
        self.expense_date_helper_text.visible = True
        self.update()
    
    def on_category_change(self, e):
        if e.control.value == "Others":
            self.other_category.visible = True
            self.update()
        else:
            self.other_category.visible = False
            self.update()
    
    def on_click(self, e):        
        self.expense_name.error_text = self.expense_amount.error_text = self.expense_category.error_text = self.other_category.error_text = ""
        
        if not self.expense_name.value:
            self.expense_name.error_text = "Please enter your expense name"
            self.update()
            return
        
        if not self.expense_amount.value:
            self.expense_amount.error_text = "Please enter your expense amount"
            self.update()
            return
        
        if not self.expense_category.value:
            self.expense_category.error_text = "Please enter your category"
            self.update()
            return
        
        if self.expense_category.value == "Others" and not self.other_category.value:
            self.other_category.error_text = "Please enter your category"
            self.update()
            return
        
        try:
            amount = int(self.expense_amount.value)
        except ValueError:
            self.expense_amount.error_text = "Please enter a valid amount"
            self.update()
            return
        
        new_expense = Expense(name=self.expense_name.value, amount=amount, category=self.expense_category.value, category_expand=self.other_category.value,date=self.expense_date, note=self.note.value)
        add_expense_to_csv(new_expense)
        
        # self.result.value = f"Adding expense..."
        self.update()
        self.page.go("/")