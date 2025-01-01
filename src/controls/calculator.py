import flet as ft

class Calculator(ft.Column):
    def __init__(self):
        super().__init__()
        
        self.input = ft.TextField(hint_text="Enter your monthly income", width=300)
        self.need_percentage = ft.TextField(value=25, width=300, suffix_text="%")
        self.save_percentage = ft.TextField(value=20, width=300, suffix_text="%")
        self.results = ft.Text("", visible=False)
        self.common_error_text = ft.Text("", color="red", visible=False)
        
        self.controls = [
            ft.Column([ft.Text("Monthly Income"), self.input]),
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
        
        if not self.input.value:
            self.input.error_text = "Please enter your monthly income"
            self.update()
            return
        
        if not self.need_percentage.value:
            self.need_percentage.error_text = "Please enter needs percentage"
            self.update()
            return
        
        if not self.save_percentage.value:
            self.save_percentage.error_text = "Please enter save percentage"
            self.update()
            return
        
        
        income = int(self.input.value)
        needs = income * (float(self.need_percentage.value) / 100)
        save = income * (float(self.save_percentage.value) / 100)
        remain = income - needs - save
        self.results.value = f"Needs: {needs:,.0f} VND, Save: {save:,.0f} VND, Remain: {remain:,.0f} VND"
        self.results.visible = True
        self.update()