import flet as ft 

class NavBar(ft.NavigationBar):
    def __init__(self, page: ft.Page, selected_index: int | None = None):
        super().__init__()
        
        self.page = page
        self.selected_index = selected_index
        
        self.destinations = [
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.ADD, label="Add Expense"),
        ]
        
        self.on_change = lambda e: self.navigate_to(e)
        
    def navigate_to(self, e):
        if e.data == "0":
            self.page.go("/")
        elif e.data == "1":
            self.page.go("/expense/new")
