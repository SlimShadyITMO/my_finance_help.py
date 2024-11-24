import matplotlib.pyplot as plt
from datetime import datetime
# import libraries


class ExpenseCategory:    #class1
    def __init__(self, name):
        self.name = name
        self.expenses = []

    def add_expense(self, amount, description):
        """"function for adding an expense to a category"""
        self.expenses.append({"amount": amount, "description": description, "date": datetime.now()})

    def get_total_expenses(self):
        """Returns the total amount of expenses in this category.
        """
        return sum(expense["amount"] for expense in self.expenses)

    def get_expenses(self):
        """"Returns a list of all expenses in the category."""
        return self.expenses


class FinancialRecord: #class2
    def __init__(self):
        """"The class constructor initializes financial records with an empty dictionary of categories, zero income and target savings."""
        self.categories = {}
        self.income = 0
        self.savings_goal = 0

    def add_income(self, amount):
        """"A function for adding income"""
        self.income += amount

    def add_expense(self, category_name, amount, description):
        """"A function for adding an expense to a specific category"""
        if category_name not in self.categories:
            self.categories[category_name] = ExpenseCategory(category_name)
        self.categories[category_name].add_expense(amount, description)

    def set_savings_goal(self, goal_amount):
        """"Sets the target amount of savings."""
        self.savings_goal = goal_amount

    def get_balance(self):
        """"Calculates the current balance by subtracting total expenses from income."""
        total_expenses = sum(category.get_total_expenses() for category in self.categories.values())
        return self.income - total_expenses

    def get_total_expenses(self):
        return sum(category.get_total_expenses() for category in self.categories.values())

    def generate_report(self):
        print("\nFinancial Report:")
        print(f"Income: {self.income}")
        print(f"Savings Goal: {self.savings_goal}")
        print(f"Current Balance: {self.get_balance()}")
        print(f"Total Expenses: {self.get_total_expenses()}")
        for category_name, category in self.categories.items():
            print(f"\nCategory: {category_name}")
            for expense in category.get_expenses():
                print(f"  - {expense['description']}: {expense['amount']} on {expense['date']}")

    def show_expense_pie_chart(self):
        category_names = list(self.categories.keys())
        expenses = [category.get_total_expenses() for category in self.categories.values()]

        if not expenses:
            print("No expenses to display.")
            return

        plt.figure(figsize=(8, 8))
        plt.pie(expenses, labels=category_names, autopct='%1.1f%%', startangle=140)
        plt.title("Expense Distribution by Category")
        plt.show()

    def show_savings_progress(self):
        current_balance = self.get_balance()
        plt.figure(figsize=(6, 6))
        plt.bar(['Savings Goal', 'Current Balance'], [self.savings_goal, current_balance], color=['blue', 'green'])
        plt.title("Savings Progress")
        plt.ylabel("Amount")
        plt.show()


def main():
    """"The function creates a class to start tracking finances."""
    financial_record = FinancialRecord()

    while True:
        print("\nMenu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Set Savings Goal")
        print("4. View Report")
        print("5. Show Expense Pie Chart")
        print("6. Show Savings Progress")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            income_amount = float(input("Enter income amount: "))
            financial_record.add_income(income_amount)
        elif choice == "2":
            category = input("Enter expense category: ")
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            financial_record.add_expense(category, amount, description)
        elif choice == "3":
            savings_goal = float(input("Enter savings goal: "))
            financial_record.set_savings_goal(savings_goal)
        elif choice == "4":
            financial_record.generate_report()
        elif choice == "5":
            financial_record.show_expense_pie_chart()
        elif choice == "6":
            financial_record.show_savings_progress()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

