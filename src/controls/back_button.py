import flet as ft

class BackButton(ft.ElevatedButton):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.page = page
        self.text = "Back"
        self.on_click = self.go_back
        
    def go_back(self, e):
        self.page.views.pop()
        self.page.go(self.page.views[-1].route)