import flet as ft 
from controls.navigation_bar import NavBar
from controls.calculator import Calculator
from dataclasses import dataclass, field
from datetime import datetime
import calendar

@dataclass
class BudgetPlan:
    budget: int
    name: str = field(default=datetime.now().strftime("%B %Y"))
    start_date: str = field(default=datetime(datetime.now().year, datetime.now().month, 1).strftime("%d/%m/%Y"))
    end_date: str = field(default=datetime(datetime.now().year, datetime.now().month, calendar.monthrange(datetime.now().year, datetime.now().month)[1]).strftime("%d/%m/%Y"))
    save_percentage: int = field(default=20)
    need_percentage: int = field(default=25)

class NewPlanView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.route = "/plan/new"
        self.navigation_bar = NavBar(page)
        self.page = page
        
        self.plan = BudgetPlan(budget=0)
        
        self.input = ft.TextField(hint_text="Enter your paycheck for this month", width=300)
        self.need_percentage = ft.TextField(value=self.plan.need_percentage, width=300, suffix_text="%")
        self.save_percentage = ft.TextField(value=self.plan.save_percentage, width=300, suffix_text="%")
        self.results = ft.Text("", visible=False)
        self.common_error_text = ft.Text("", color="red", visible=False)
        
        self.controls = [
            ft.Text("Create Plan"),
            ft.Column([ft.Text("Paycheck"), self.input]),
            ft.Row([
                ft.Column([ft.Text("Needs (%)"), self.need_percentage]),
                ft.Column([ft.Text("Save (%)"), self.save_percentage]),
            ]),
            self.results,
            self.common_error_text,
            ft.ElevatedButton("Calculate", on_click=self.on_click),
        ]
        
    def on_click(self, e):
        self.input.error_text = self.need_percentage.error_text = self.save_percentage.error_text = ""
        
        if not self.input.value or self.input.value == "0":
            self.input.error_text = "Please enter your paycheck"
            self.update()
            return
        
        try:
            int(self.input.value)
        except ValueError:
            self.input.error_text = "Please enter a valid number"
            self.update()
            return
        if not self.need_percentage.value or self.need_percentage.value == "0":
            self.need_percentage.error_text = "Please enter needs percentage"
            self.update()
            return
        
        if not self.save_percentage.value or self.save_percentage.value == "0":
            self.save_percentage.error_text = "Please enter save percentage"
            self.update()
            return
        
        self.calculate(e)
        
        self.controls.pop()
        self.controls.extend(
            [
                ft.ElevatedButton("Reset", on_click=self.reset),
                ft.ElevatedButton("Calculate", on_click=self.calculate),
                ft.ElevatedButton("Save", on_click=lambda e: print(self.plan.__dict__))
            ]
        )
        
        self.update()
        
    def calculate(self, e):
        budget = int(self.input.value)
        self.plan.budget = budget
        self.plan.need_percentage = int(self.need_percentage.value)
        self.plan.save_percentage = int(self.save_percentage.value)
        
        needs = budget * (float(self.need_percentage.value) / 100)
        save = budget * (float(self.save_percentage.value) / 100)
        remain = budget - needs - save
        
        self.results.value = f"Needs: {needs:,.0f} VND, Save: {save:,.0f} VND, Remain: {remain:,.0f} VND"
        self.results.visible = True
        
        self.update()
        
    def reset(self, e):
        self.plan.budget = 0
        self.plan.need_percentage = 25
        self.plan.save_percentage = 20
        self.input.value = ""
        self.need_percentage.value = 25
        self.save_percentage.value = 20
        self.results.visible = False
        self.controls.pop()
        self.controls.pop()
        self.controls.pop()
        self.controls.append(ft.ElevatedButton("Calculate", on_click=self.on_click))
        self.update()
        