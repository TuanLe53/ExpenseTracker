import flet as ft

class Calculator(ft.Column):
    def __init__(self):
        super().__init__()
        
        self.input = ft.TextField(hint_text="Enter your monthly income", width=300)
        self.need_percentage = ft.TextField(value=0.25, width=300)
        self.save_percentage = ft.TextField(value=0.2, width=300)
        self.results = ft.Text("")
        
        self.controls = [
            self.input,
            ft.Row([self.need_percentage, self.save_percentage]),
            self.results,
            ft.ElevatedButton("Calculate", on_click=self.on_click),
        ]
        
    def on_click(self, e):
        income = int(self.input.value)
        needs = income * float(self.need_percentage.value)
        save = income * float(self.save_percentage.value)
        self.results.value = f"Needs: {needs:,.0f} VND, Save: {save:,.0f} VND"
        self.update()