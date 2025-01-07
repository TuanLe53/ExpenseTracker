import flet as ft
from views.home import HomeView
from views.new_plan import NewPlanView
from controls.calculator import Calculator
from db.db import create_tables
from controls.add_expense import AddExpense
from controls.navigation_bar import NavBar

def main(page: ft.Page):
    page.title = "Tracker"
    
    create_tables()

    def route_change(route):
        page.views.clear()
        page.views.append(HomeView(page))
        
        if page.route == "/expense/new":
            page.views.append(
                ft.View(
                    "/expense/new",
                    [
                        AddExpense(page),
                    ],
                    navigation_bar=NavBar(page)
                )
            )
        elif page.route == "/calculate":
            page.views.append(
                ft.View(
                    "/calculate",
                    [
                        Calculator(),
                    ],
                    navigation_bar=NavBar(page)
                )
            )
        elif page.route == "/plan/new":
            page.views.append(NewPlanView(page))
            
        page.update()
        
    def view_pop(view):
        page.views.pop(view)
        top_view = page.views[-1]
        page.go(top_view.route)
        
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    
ft.app(main)