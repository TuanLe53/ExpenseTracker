from peewee import IntegrityError, DoesNotExist
from db.db import db, PlanModel

def add_plan(
    name: str, 
    budget: int, 
    start_date: str, 
    end_date: str, 
    save_percentage: int, 
    need_percentage: int, 
    is_active: bool
) -> None:
    """
    Add a new plan to the database.
    
    :param name: Name of the plan
    :param budget: Budget for the plan
    :param start_date: Start date of the plan (YYYY-MM-DD)
    :param end_date: End date of the plan (YYYY-MM-DD)
    :param save_percentage: Percentage of budget allocated for saving
    :param need_percentage: Percentage of budget allocated for needs
    :param is_active: Whether the plan is active
    """
    try:
        with db.atomic():
            PlanModel.create(
                name=name,
                budget=budget,
                start_date=start_date,
                end_date=end_date,
                save_percentage=save_percentage,
                need_percentage=need_percentage,
                is_active=is_active,
            )
    except IntegrityError:
        print("An error has occurred when create new plans")

def get_active_plan() -> PlanModel | None:
    """
    Retrieve the active plan from the database.

    :return: The active PlanModel instance or None if not found
    """
    try:
        return PlanModel.select().where(PlanModel.is_active == True).get()
    except DoesNotExist:
        return None

def close_plan() -> None:
    """
    Mark the currently active plan as inactive.
    """
    plan = get_active_plan()
    if plan:
        try:
            with db.atomic():
                plan.is_active = False
                plan.save()
        except Exception as e:
            print("Failed to close the plan")
    else:
        print("No active plan to close.")
