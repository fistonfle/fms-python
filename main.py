#!/usr/bin/env python3
# main.py
from utils import add_expense, add_crop, edit_crop, display_expenses, display_crops, signup, login, load_users, save_users, load_expenses, load_crops, reset_password

CROPS_FILE = "crops.txt"

EXPENSES_FILE = "expenses.txt"

# Initialize expenses and crops lists
expenses = []
crops = []

# Initialize users dictionary
users = {}

# Define the filename for storing user data
USERS_FILE = "users.txt"

# Load users from file
users = load_users(USERS_FILE)

# Load expenses from file
expenses = load_expenses(EXPENSES_FILE)

# Load crops from file
crops = load_crops(CROPS_FILE)

# Function to login an existing user
def login_user(username, password):
    if username not in users or users[username] != password:
        print("Invalid username or password. Please try again.")
        return False
    else:
        print("Login successful. Welcome back, {}!".format(username))
        return True

# Main function to handle user interaction
def main():
    logged_in = False
    while True:
        print("\nFarm Management System (FMS)")
        if not logged_in:
            print("1. Signup")
            print("2. Login")
            print("3. Forgot Password,reset")
        else:
            print("1. Add Expense")
            print("2. Add Crop")
            print("3. View Expenses")
            print("4. View Crops")
            print("5. Edit Crop")
            print("6. Logout")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            if not logged_in:
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                signup(users, username, password)
                save_users(users, USERS_FILE)
            else:
                amount = float(input("Enter the amount: "))
                category = input("Enter the category: ")
                description = input("Enter the description: ")
                add_expense(expenses, amount, category, description, EXPENSES_FILE)  # Call function to add expense
        elif choice == '2':
            if not logged_in:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                logged_in = login_user(username, password)
            else:
                name = input("Enter the name of the crop: ")
                planting_date = input("Enter the planting date: ")
                variety = input("Enter the variety: ")
                add_crop(crops, name, planting_date, variety, CROPS_FILE)
               
        elif choice == '3':
            if logged_in:
                display_expenses(expenses)
            else:
                print("Forgot password, reset")
                reset_password(users)
        elif choice == '4':
            if logged_in:
                display_crops(crops)  # Call function to display crops
      elif choice == '5':
            if logged_in:
                if crops:
                    display_crops(crops)
                    name = input("Enter the name of crop to edit: ")
                    if 0 <= name < len(crops):
                        new_name = input("Enter the new name: ")
                        new_planting_date = input("Enter the new planting date: ")
                        new_variety = input("Enter the new variety: ")
                        edit_crop(crops, index, new_name, new_planting_date, new_variety, CROPS_FILE)
                    else:
                        print("Invalid name of crop.Try again")
                else:
                    print("No crops to edit.")
      elif choice == '6':
            if logged_in:
                print("Logging out...")
                logged_in = False
            else:
                print("Invalid choice. Please try again.")
        elif choice == '7':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
