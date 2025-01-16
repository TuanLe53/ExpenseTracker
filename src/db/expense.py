from peewee import IntegrityError
from db.db import db, ExpenseModel
from db.plan import get_active_plan
from typing import List

def add_expense(
    name: str, 
    amount: float, 
    category: str, 
    date: str, 
    category_expand: str, 
    note: str, 
    plan: int
) -> None:
    """
    Add a new expense to the database.

    :param name: Name of the expense
    :param amount: Amount spent
    :param category: Category of the expense
    :param date: Date of the expense (YYYY-MM-DD)
    :param category_expand: Additional category details
    :param note: A note about the expense
    :param plan: ID of the plan associated with the expense
    """
    try:
        with db.atomic():
            ExpenseModel.create(
                name=name,
                amount=amount,
                category=category,
                date=date,
                category_expand=category_expand,
                note=note,
                plan=plan,
            )
    except IntegrityError:
        print("Failed to add expense")

def get_expenses_from_current_plan() -> List[ExpenseModel]:
    """
    Retrieve all expenses associated with the active plan.

    :return: A list of expenses for the active plan or None if no active plan exists
    """
    plan = get_active_plan()
    if plan:
        try:
            return plan.expenses  # Assuming a reverse relation is set up in Peewee for `ExpenseModel.plan`
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    return []