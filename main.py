# Function to save expenses to a text file
def save_expenses():
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write("{},{},{}\n".format(expense['amount'], expense['category'], expense['description']))

# Function to save crops to a text file
def save_crops():
    with open("crops.txt", "w") as file:
        for crop in crops:
            file.write("{},{},{}\n".format(crop['name'], crop['planting_date'], crop['variety']))

# Function to load expenses from a text file
def load_expenses():
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                amount, category, description = line.strip().split(',')
                expenses.append({"amount": float(amount), "category": category, "description": description})
    except FileNotFoundError:
        # If the file doesn't exist, there are no expenses yet
        pass

# Function to load crops from a text file
def load_crops():
    try:
        with open("crops.txt", "r") as file:
            for line in file:
                name, planting_date, variety = line.strip().split(',')
                crops.append({"name": name, "planting_date": planting_date, "variety": variety})
    except FileNotFoundError:
        # If the file doesn't exist, there are no crops yet
        pass

# Main function to handle user input and interaction
def main():
    # Load existing data from text files
    load_expenses()
    load_crops()

    while True:
        print("\nFarm Management System (FMS)")
        print("1. Add Expense")
        print("2. Add Crop")
        print("3. View Expenses")
        print("4. View Crops")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            description = input("Enter expense description: ")
            add_expense(amount, category, description)
            save_expenses()  # Save expenses to text file
        elif choice == '2':
            name = input("Enter crop name: ")
            planting_date = input("Enter planting date: ")
            variety = input("Enter crop variety: ")
            add_crop(name, planting_date, variety)
            save_crops()  # Save crops to text file
        elif choice == '3':
            display_expenses()
        elif choice == '4':
            display_crops()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
