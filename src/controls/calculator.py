import flet as ft

class Calculator(ft.Row):
    def __init__(self):
        super().__init__()
        
        self.input = ft.TextField(hint_text="Enter your monthly income", width=300)
        self.results = ft.Text("")
        
        self.controls = [
            self.input,
            ft.ElevatedButton("Calculate", on_click=self.on_click),
            self.results
        ]
        
    def on_click(self, e):
        income = int(self.input.value)
        needs = income * 0.25
        save = income * 0.2
        self.results.value = f"Needs: {needs:,} VND, Save: {save:,} VND"
        self.update()