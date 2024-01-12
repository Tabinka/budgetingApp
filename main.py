# Kakeibo Budget Planner
import csv
from datetime import datetime

def add_expense():
    category = input("What category: ")
    name = input("Name of expense: ")
    money = input("How much spend? ")
    # Code to add an expense
    with open('file.csv', 'w+') as f:
        writer = csv.writer(f)
        writer.writerow([category,name,money,datetime.now()])

def view_expenses():
    # Code to view expenses
    with open('file.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(f"Category: {row[0]}, name: {row[1]}, how much: {row[2]}, date: {row[3]}")

def set_budget():
    # Code to set monthly budget
    monthly_budget = input("What is your monthly budget? ")
    budget_category = input("For what category? ")
    with open('budget.csv', 'w+') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.today().month, monthly_budget, budget_category])

#def view_reports():
    # Code to generate and view reports

def main_menu():
    print("1) Add expenses \n 2) View expenses \n 3) Set budget \n 4) View reports\n")
    user_input = input("What is your choice? ")
    if user_input == "1":
        add_expense()
    elif user_input == "2":
        view_expenses()
    elif user_input == "3":
        set_budget()

if __name__ == "__main__":
    main_menu()
