import flet as ft
from controls.navigation_bar import NavBar
from db.plan import get_active_plan, close_plan

class HomeView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.page = page
        self.navigation_bar = NavBar(self.page, 0)
        
        self.plan = get_active_plan()
        
        self.controls = []
        
        
    def did_mount(self):
        if self.plan == None:
            self.controls = [
                ft.Text("You have no active plan. Press the button below to create a new plan"),
                ft.ElevatedButton("Create Plan", on_click=lambda e: self.page.go("/plan/new"))
            ]
            self.update()
        else:            
            self.controls = [
                ft.Text(self.plan.name),
                ft.Text(f"Total: {self.plan.budget:,.0f}"),
                ft.Row([
                    ft.Text(f"Need: {self.plan.need_percentage}%"),
                    ft.Text(f"Save: {self.plan.save_percentage}%")
                ]),
                ft.ElevatedButton("Close plan", on_click=self.finish_plan)
            ]
            
            
            self.update()
            
    def finish_plan(self, e):
        close_plan()
        self.controls = [
            ft.Text("You have no active plan. Press the button below to create a new plan"),
            ft.ElevatedButton("Create Plan", on_click=lambda e: self.page.go("/plan/new"))
        ]
        self.update()