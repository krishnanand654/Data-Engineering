from collections import defaultdict
import datetime

#Expense enitity
class expenseTracker:
    def __init__(self, expense_id, date, category,description, amount):
        self.expense_id = expense_id
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount
    def __str__(self):
        return(f"{self.expense_id:<5}|\t{self.date:<12}|\t{self.category:<12}|\t{self.description:<15}|{self.amount:>5}")

#Expense store
expenses=[]

#insert
def add_expense(expense):
    expenses.append(expense)
    print(f"\n{'*'*5}Expense Added successfully{'*'*5}\n")
    return True
#delete
def delete_expense(expense_id):
    for expense in expenses:
        if expense_id == expense.expense_id:
            expenses.remove(expense)
            return True
        else:
            print("Item not found")
#update
def update_expense(expense_id, new_expense):
    for expense in expenses:
        if expense_id == expense.expense_id:
            expense.date = new_expense.date
            expense.category = new_expense.category
            expense.description = new_expense.description
            expense.amount = new_expense.amount
            return True
    return False
#view
def display_expense():
    print(f"\n{'ID':<5}|\t{'Date':<12}|\t{'Category':<12}|\t{'Description':<15}|{'Amount':>8}")
    print(f"{'-'*70}")
    if len(expenses) <= 0:
        print("No items")
    else:
        for i in expenses:
            print(i)

expense = expenseTracker("101", '20/10/2001', 'travel','bus ride', 10)
expense2 = expenseTracker("102", '20/10/2001', 'travel','bus ride', 10)
expense3 = expenseTracker("103", '20/10/2001', 'travel','bus ride', 10)
 
# add_expense(expense)
# add_expense(expense2)
# add_expense(expense3)


#user cred store
user_db = {'username':'admin', 'password':'root'}
#user login
def authenticate_user(username, password):
    if username == user_db['username'] and password == user_db['password']:
        print("Login Successful")
        return True
    else:
        print(f"\n{'!'*5} Login failed {'!'*5}\n")
        return False
    
#catergory and its expenses
def categorize_expenses():
    #default dict to handle the KeyError while updating the amount
    categories = defaultdict(int)
    for expense in expenses:
        categories[expense.category] += expense.amount
    return categories

#Total amount
def  summarize_expenses():
    total = 0
    for expense in expenses:
        total += expense.amount
    return total

#Total amount
def calculate_total_expenses():
    return sum(expense.amount for expense in expenses)

#generate summary
def generate_summary_report():
    data = dict(categorize_expenses())
    print(f"\n{'Category':<10}| {'Total Expense':>15}")
    print("-"*30)
    for category, expense in data.items():
        print(f"{category:<10}|{expense:>10}")
    print("\nTotal Expense: ", calculate_total_expenses())


def cli():
    while True:
        print(f"\n\n{'-'*5}Menu{'-'*5}")
        print('''\n1. Add an expense
              \n2. Update an expense
              \n3. Delete expense
              \n4. Displays all expenses
              \n5. Generate summary report
              \n6. Logout and Exit''')
        ch = int(input("\nEnter choice: "))

        if ch == 1:
            expense_id = input("Enter expense_id: ")
            found = False
            for expense in expenses:
                if expense_id == expense.expense_id:
                    found = True
            if found:
                print(f"\n{'!'*5} Id already exist {'!'*5}")
            else:
                date = input("Enter date in DD/MM/YYYY format: ")
                category = input("Enter category: ")
                description = input("Enter description: ")
                while True:
                    try:
                        amount = int(input("Enter amount: "))
                        expense = expenseTracker(expense_id, date, category, description, amount)
                        if add_expense(expense):
                            break
                    except ValueError as e:
                        print(f"\n{'!'*5} Invalid price format {'!'*5}\n")

        elif ch == 2:
            expense_id = input("Enter expense_id: ")
            found = False
            for expense in expenses:
                if expense_id == expense.expense_id:
                    found = True
            if found:
                date = input("Enter date in DD/MM/YYYY format: ")
                category = input("Enter category: ")
                description = input("Enter description: ")
                while True:
                    try:
                        amount = int(input("Enter amount: "))
                        new_expense = expenseTracker(expense_id, date, category, description, amount)
                        if not update_expense(expense_id, new_expense):
                            print(f"\n{'!'*5} Expense not found {'!'*5}")
                        else:
                            print(f"\n{'-'*5} Expense updated successfully {'-'*5}")
                    except ValueError as e:
                        print(f"\n{'!'*5} Invalid price format {'!'*5}\n")
                    break
            else:
                print(f"\n{'!'*5} Expense not found {'!'*5}")
        elif ch == 3:
            found = False
            expense_id = input("Enter expense id: ")
            for expense in expenses:
                if expense.expense_id == expense_id:
                    found = True
            if found:
                if delete_expense(expense_id):
                    print(f"\n{'*'*5}Expense deleted successfully{'*'*5}")
            else:
                print(f"\n{'*'*5}Expense not found{'*'*5}")
        elif ch == 4:
            display_expense()
        elif ch == 5:
            generate_summary_report()
        elif ch == 6:
            print("\nLogging out and exiting applicaiton...\n")
            break
        else:
            print("\nInvalid choice")
#login
def login():
    print(f"\n{'-'*5}LOGIN{'-'*5}\n")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if authenticate_user(username, password):
        cli()
        
if __name__ == '__main__':
    login()