import datetime
import sqlite3

con = sqlite3.connect("expenses.db")
cur = con.cursor()

while True:
    print("1.New expense")
    print("2.View monthly expenses")

    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        date = input("Choose a date: ")
        description = input("Input a description: ")

        cur.execute("SELECT DISTINCT category FROM expenses")
        categories = cur.fetchall()

        for idx, category in enumerate(categories):
            print(f"{idx + 1}.{category[0]}")
        print(f"{len(categories) + 1}. Create a new category")

        try:
            cat_choice = int(input())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if cat_choice == len(categories) + 1:
            category = input("Enter a new category name: ")
        else:
            category = categories[cat_choice - 1][0]

        try:
            price = int(input("Input the price: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        cur.execute(
            "INSERT INTO expenses (Date, description, category, price) VALUES (?,?,?,?)",
            (date, description, category, price),
        )
        con.commit()
    elif choice == 2:
        print("Select an option")
        print("1. View all expenses")
        print("2. View monthly expenses")

        try:
            option = int(input())
        except ValueError:
            print("Please enter a number: ")
            continue
        if option == 1:
            cur.execute("SELECT * FROM EXPENSES")
            expenses = cur.fetchall()
            for expense in expenses:
                print(expense)
        elif option == 2:
            month = input("Enter the month: ")
            year = input("Enter the year: ")
            cur.execute(
                "SELECT category, SUM(price) FROM expenses WHERE strftime('%m', Date) = ? AND strftime('%Y', Date) = ? GROUP BY category",
                (month, year),
            )
            expenses = cur.fetchall()

            if(len(expenses) == 0):
                print(f"No expenses in {month}. ")
            else:
                for expense in expenses:
                    print(f"Category:{expense[0]}, Expense:{expense[1]}")
        else:
            print("Please choose an existing option.")
            continue
    else:
        print("Please choose an existing option.")
        continue
    repeat = input("Would you like to do anything else? Y/N ")
    if repeat.lower() != "y":
        break
con.close()
