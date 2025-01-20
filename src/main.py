import flet as ft
from views.home import HomeView
from views.new_plan import NewPlanView
from views.new_expense import NewExpenseView
from views.expenses import ExpensesView
from db.db import create_tables

def main(page: ft.Page):
    page.title = "Tracker"
    
    create_tables()

    def route_change(route):
        page.views.clear()
        page.views.append(HomeView(page))
        
        if page.route == "/expense/new":
            page.views.append(NewExpenseView(page))
        elif page.route == "/plan/new":
            page.views.append(NewPlanView(page))
        elif page.route == "/plan/expenses":
            page.views.append(ExpensesView(page))
            
        page.update()
        
    def view_pop(view):
        page.views.pop(view)
        top_view = page.views[-1]
        page.go(top_view.route)
        
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    
ft.app(main)