import flet as ft

class AddIncome(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.page = page
        
        self.name = ft.TextField(hint_text="Enter your income name", width=300)
        self.income_amount = ft.TextField(hint_text="Enter your monthly income", width=300)
        self.date = ft.DatePicker()
        
        self.controls = [
            ft.Column([ft.Text("Income Name"), self.name]),
            ft.Column([ft.Text("Monthly Income"), self.income_amount]),
            ft.ElevatedButton("Add Income", on_click=self.on_click)
        ]
        
    def on_click(self, e):
        print(e)