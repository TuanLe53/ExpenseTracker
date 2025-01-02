import uuid
from csv import writer
from dataclasses import dataclass, field
from typing import Optional
import os

@dataclass
class Expense:
    name: str
    amount: int
    category: str
    date: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    category_expand: Optional[str] = field(default=None)
    note: Optional[str] = field(default=None)
    

def add_expense_to_csv(expense: Expense):
    file_path = os.path.join(os.path.dirname(__file__), 'expenses.csv')

    with open(file_path, 'a') as f:
        w = writer(f, lineterminator='\n')
        w.writerow([expense.id, expense.name, expense.amount, expense.category, expense.category_expand, expense.date, expense.note])
        f.close()