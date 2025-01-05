import uuid
from csv import writer, reader
from dataclasses import dataclass, field
from typing import Optional
import os
from .utils import write_csv_file

@dataclass
class Expense:
    name: str
    amount: int
    category: str
    date: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    category_expand: Optional[str] = field(default=None)
    note: Optional[str] = field(default=None)
    
file_path = os.path.join(os.path.dirname(__file__), 'expenses.csv')

def add_expense_to_csv(expense: Expense) -> None:

    with open(file_path, 'a') as f:
        w = writer(f, lineterminator='\n')
        w.writerow([expense.id, expense.name, expense.amount, expense.category, expense.category_expand, expense.date, expense.note])
        f.close()
        
def get_expenses() -> list[Expense]:
    expenses: list[Expense] = []
    with open(file_path, 'r') as f:
        r = reader(f)
        
        next(r, None)
        
        for row in r:
            expense = Expense(id=row[0], name=row[1], amount=row[2], category=row[3], category_expand=row[4], date=row[5], note=row[6])
            expenses.append(expense)        
        
    return expenses

def delete_expense_by_id(expense_id: uuid.UUID) -> None:
    expenses = get_expenses()
    expenses = [expense for expense in expenses if expense.id != expense_id]
    
    columns = ['id', 'name', 'amount', 'category', 'category_expand', 'date', 'note']
    
    write_csv_file(
        file_path,
        columns,
        [[expense.id, expense.name, expense.amount, expense.category, expense.category_expand, expense.date, expense.note] for expense in expenses]
    )