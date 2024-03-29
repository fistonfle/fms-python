# utils.py

# Function to save users to a text file
def save_users(users, filename):
    with open(filename, "w") as file:
        for username, password in users.items():
            file.write("{},{}\n".format(username, password))

# Function to load users from a text file
def load_users(filename):
    users = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                username, password = line.strip().split(',')
                users[username] = password
    except FileNotFoundError:
        # If the file doesn't exist, return an empty dictionary
        pass
    return users


# Function to add an expense and store it in a text file
def add_expense(expenses, amount, category, description, filename):
    expenses.append({"amount": amount, "category": category, "description": description})
    with open(filename, "a") as file:
        file.write("{},{},{}\n".format(amount, category, description))

# Function to add a crop and store it in a text file
def add_crop(crops, name, planting_date, variety, filename):
    crops.append({"name": name, "planting_date": planting_date, "variety": variety})
    with open(filename, "a") as file:
        file.write("{},{},{}\n".format(name, planting_date, variety))


# Function to load expenses from a text file
def load_expenses(filename):
    expenses = []
    try:
        with open(filename, "r") as file:
            for line in file:
                amount, category, description = line.strip().split(',')
                expenses.append({"amount": amount, "category": category, "description": description})
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        pass
    return expenses

# Function to load crops from a text file
def load_crops(filename):
    crops = []
    try:
        with open(filename, "r") as file:
            for line in file:
                name, planting_date, variety = line.strip().split(',')
                crops.append({"name": name, "planting_date": planting_date, "variety": variety})
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        pass
    return crops

# Function to display all expenses
def display_expenses(expenses):
    print("---- Expenses ----")
    for expense in expenses:
        print("Amount: {}, Category: {}, Description: {}".format(expense['amount'], expense['category'], expense['description']))

# Function to display all crops
def display_crops(crops):
    print("---- Crops ----")
    for crop in crops:
        print("Name: {}, Planting Date: {}, Variety: {}".format(crop['name'], crop['planting_date'], crop['variety']))


# Function to signup a new user
def signup(users, username, password):
    if username in users:
        print("Username already exists. Please choose a different username.")
        return False
    else:
        users[username] = password
        print("Signup successful. Welcome, {}!".format(username))
        return True
    
# Function to login an existing user
def login(users, username, password):
    if username not in users or users[username] != password:
        print("Invalid username or password. Please try again.")
        return False
    else:
        print("Login successful. Welcome back, {}!".format(username))
        return True
    
# Function to logout a user
def logout():
    print("Logging out...")
    return False
