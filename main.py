
import pandas as pd
from datetime import datetime
import os

FILE_NAME = "expenses.csv"

if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Name", "Amount", "Category"])
    df.to_csv(FILE_NAME, index=False)

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount (₹): "))
    category = input("Enter category (food, travel, etc): ")
    date = datetime.now().strftime("%Y-%m-%d")

    new_expense = pd.DataFrame([[date, name, amount, category]],
                               columns=["Date", "Name", "Amount", "Category"])
    df = pd.read_csv(FILE_NAME)
    df = pd.concat([df, new_expense], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)
    print("Expense added successfully.\n")

def view_expenses():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No expenses recorded yet.\n")
    else:
        print("\nYour Expenses:\n")
        print(df.to_string(index=False))
        print()

def total_spent():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No expenses yet.\n")
    else:
        total = df["Amount"].sum()
        print(f"Total spent so far: ₹{total}\n")

while True:
    print("------ Expense Tracker ------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spent")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_spent()
    elif choice == "4":
        print("Goodbye.")
        break
    else:
        print("Invalid choice, try again.\n")