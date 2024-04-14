#!/usr/bin/env python3
# main.py
from utils import (
    add_expense,
    add_crop,
    display_expenses,
    display_crops,
    register_category,
    view_categories,
    edit_expense,
    delete_expense,
    edit_crop,
    delete_crop,
    generate_expense_report,
    generate_crop_report,
    load_users,
    signup,
    login,
    edit_user,
    load_expenses,
    load_crops,
    load_categories
)

import os
import platform
import getpass

CROPS_FILE = "crops.txt"
EXPENSES_FILE = "expenses.txt"
CATEGORIES_FILE = "categories.txt"
USERS_FILE = "users.txt"

# Initialize expenses, crops, and categories lists
expenses = []
crops = []
categories = []

# Load users from file
users = load_users(USERS_FILE)

# Load expenses from file
expenses = load_expenses(EXPENSES_FILE)

# Load crops from file
crops = load_crops(CROPS_FILE)

# Load categories from file
categories = load_categories(CATEGORIES_FILE)

def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

 # Function to input password securely
def get_password(prompt="Password: "):
    return getpass.getpass(prompt)



# Main function to handle user interaction
def main():
    logged_in = False
    while True:
        clear_terminal()
        print("\nFarm Management System (FMS)")
        if not logged_in:
            print("1. Signup")
            print("2. Login")
            print("3. Exit")
        else:
            print("1. Add Expense")
            print("2. Add Crop")
            print("3. View Expenses")
            print("4. View Crops")
            print("5. Register Category")
            print("6. View Categories")
            print("7. Edit Expense")
            print("8. Delete Expense")
            print("9. Edit Crop")
            print("10. Delete Crop")
            print("11. Generate Expense Report")
            print("12. Generate Crop Report")
            print("13. Edit User Information")
            print("14. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            if not logged_in:
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                signup(users, username, password, USERS_FILE)
            else:
                amount = float(input("Enter the amount: "))
                category = input("Enter the category: ")
                description = input("Enter the description: ")
                add_expense(expenses, amount, category, description, EXPENSES_FILE, categories)
        elif choice == '2':
            if not logged_in:
                username = input("Enter your username: ")
                password = get_password("Enter your password: ")
                logged_in = login(users, username, password)
            else:
                name = input("Enter the name of the crop: ")
                planting_date = input("Enter the planting date: ")
                variety = input("Enter the variety: ")
                category = input("Enter the category: ")
                add_crop(crops, name, planting_date, variety, category, CROPS_FILE, categories)
        elif choice == '3':
            if logged_in:
                display_expenses(expenses, categories)
        elif choice == '4':
            if logged_in:
                display_crops(crops, categories)
        elif choice == '5':
            if logged_in:
                category = input("Enter the new category: ")
                register_category(categories, category, CATEGORIES_FILE)
        elif choice == '6':
            if logged_in:
                view_categories(categories)
        elif choice == '7':
            if logged_in:
                edit_expense(expenses, EXPENSES_FILE)
                pass
        elif choice == '8':
            if logged_in:
                delete_expense(expenses, EXPENSES_FILE)
                pass
        elif choice == '9':
            if logged_in:
                edit_crop(crops, CROPS_FILE)
                pass
        elif choice == '10':
            if logged_in:
                delete_crop(crops, CROPS_FILE)
                pass
        elif choice == '11':
            if logged_in:
                generate_expense_report(expenses, categories)
        elif choice == '12':
            if logged_in:
                generate_crop_report(crops, categories)
        elif choice == '13':
            if logged_in:
                edit_user(users, USERS_FILE)
        elif choice == '14':
            if logged_in:
                print("Logging out...")
                logged_in = False
        elif choice == '15':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

        input("Press Enter to continue...")

# Entry point of the program
if __name__ == "__main__":
    main()
