import flet as ft 

class NavBar(ft.NavigationBar):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.page = page
        
        self.destinations = [
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.ADD, label="Add Expense"),
            ft.NavigationBarDestination(icon=ft.Icons.CALCULATE_ROUNDED, label="Calculate"),
        ]
        
        self.on_change = lambda e: self.navigate_to(e)
        
    def navigate_to(self, e):
        if e.data == "0":
            self.page.go("/")
        elif e.data == "1":
            self.page.go("/expense/new")
        elif e.data == "2":
            self.page.go("/calculate")