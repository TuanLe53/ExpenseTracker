import flet as ft
from controls.navigation_bar import NavBar
from db.plan import get_active_plan

class HomeView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.page = page
        self.route = "/"
        self.navigation_bar = NavBar(self.page)
        self.controls = []
        
        
    def did_mount(self):
        if not get_active_plan():
            self.controls = [
                ft.Text("You have no active plan. Press the button below to create a new plan"),
                ft.ElevatedButton("Create Plan", on_click=lambda e: self.page.go("/plan/new"))
            ]
            self.update()
        else:
            self.controls = [
                ft.Text("Welcome to Tracker"),
                ft.Text("This is a simple expense tracker app"),
                ft.Text("You can start by adding your income and expenses"),
                ft.Text("You can also calculate your expenses"),
            ]
            self.update()