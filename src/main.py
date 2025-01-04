import flet as ft
from controls.expense_list import ExpenseList
from db_csv.expense import get_expenses
from controls.add_expense import AddExpense

def main(page: ft.Page):
    page.title = "Expenses Tracker"

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.ADD, label="Add Expense"),
        ],
        on_change=lambda e: navigate_to(e)
    )

    def navigate_to(e: ft.ControlEvent):
        if e.data == "0":
            page.go("/")
        elif e.data == "1":
            page.go("/expense/new")


    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ExpenseList(get_expenses()),
                ],
                navigation_bar=page.navigation_bar
            )
        )
        
        if page.route == "/expense/new":
            page.views.append(
                ft.View(
                    "/expense/new",
                    [
                        AddExpense(page),
                    ],
                    navigation_bar=page.navigation_bar
                )
            )
            
        page.update()
        
    def view_pop(view):
        page.views.pop(view)
        top_view = page.views[-1]
        page.go(top_view.route)
        
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    
ft.app(main)