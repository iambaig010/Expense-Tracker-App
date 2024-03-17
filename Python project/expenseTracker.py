from expense import Expense
import calendar
import datetime



def main():
    print("running")
    expenseFilePath = "expenses.csv"
    budget = 10000

    # Get users to input their expense
    expense = getUsersExpenses()

    #Write it to a file
    saveExpensesToFile(expense, expenseFilePath)

    #Read the file and summerise the expenses
    summeriseExpenses(expenseFilePath, budget)


def getUsersExpenses():
    print("Getting user expenses")
    expenseName = input("Enter expense name:")
    expenseAmount = float(input("Enter expense amount:"))
    expenseCateories = [
        "🍔 Food", 
        "🏠 Home", 
        "💼 Work", 
        "💃🏼 Fun", 
        "✨ Misc"
    ]

    while True:
        print("Select a category: ")
        for i, categoryName in enumerate(expenseCateories):
            print(f" {i + 1}. {categoryName}")

        valueRange = f"[1 - {len(expenseCateories)}]"
        selectedIndex = int(input(f"Enter a category number {valueRange}: ")) - 1

        if selectedIndex in range(len(expenseCateories)):
            slectedCategory = expenseCateories[selectedIndex]
            newExpense = Expense(
                name=expenseName, category=slectedCategory, amount=expenseAmount
            )
            return newExpense
        else:
            print("Invalid category. Please Try again")


def saveExpensesToFile(expense: Expense, expenseFilePath):
    print(f"Saving user expenses: {expense} to {expenseFilePath}")
    with open(expenseFilePath, "a") as f:
        f.write(f"{expense.category},{expense.name},{expense.amount}\n")

    

def summeriseExpenses(expenseFilePath, budget):
    print("Summerising user expenses")
    expenses: list[Expense] = []
    with open(expenseFilePath, "r") as f:
        lines = f.readlines()
        for line in lines:
            expenseCategory, expenseName, expenseAmount  = line.strip().split(",")
            lineExpense = Expense(
                name= expenseName, amount= float(expenseAmount), category=expenseCategory
            )
            expenses.append(lineExpense)

    amountByCategory = {}
    for expense in expenses:
        key = expense.category
        if key in amountByCategory:
            amountByCategory[key] += expense.amount
        else:
            amountByCategory[key] = expense.amount

    print("Expense By Category")
    for key, amount in amountByCategory.items():
        print(f" {key}: ₹{amount:.2f}")

    totalSpent = sum([ex.amount for ex in expenses])
    print(f"Total Spent ₹{totalSpent:.2f} this month ")

    remainingBudget = budget - totalSpent
    print(f"Budget remaining ₹{remainingBudget:.2f} for this month ")

    now = datetime.datetime.now()
    daysInMonth = calendar.monthrange(now.year, now.month)[1]
    remainingDays = daysInMonth - now.day

    dailyBudget = remainingBudget / remainingDays
    print(green(f"You can spend ₹{dailyBudget:.2f} per day for the remaing month"))

def green(text):
    return f"\033[92m{text}\033[0m"

if __name__ == "__main__":
    main()