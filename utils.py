from prettytable import PrettyTable

# Function to save users to a text file
def save_users(users, filename):
    with open(filename, "w") as file:
        for user_id, (username, password) in users.items():
            file.write("{},{},{}\n".format(user_id, username, password))

# Function to load users from a text file
def load_users(filename):
    users = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                user_id, username, password = line.strip().split(',')
                users[user_id] = (username, password)
    except FileNotFoundError:
        # If the file doesn't exist, return an empty dictionary
        pass
    return users


# Function to save categories to a text file
def save_categories(categories, filename):
    with open(filename, "w") as file:
        for category_id, category in categories.items():
            file.write("{},{}\n".format(category_id, category))

# Function to load categories from a text file
def load_categories(filename):
    categories = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                category_id, category = line.strip().split(',')
                categories[category_id] = category
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        pass
    return categories

# Function to register a new category
def register_category(categories, category, filename):
    if category in categories.values():
        print("Category already exists.")
        return False
    else:
        category_id = str(len(categories) + 1)
        categories[category_id] = category
        with open(filename, "a") as file:
            file.write("{},{}\n".format(category_id, category))
        print("Category '{}' registered successfully.".format(category))
        return True

# Function to view all registered categories
def view_categories(categories):
    table = PrettyTable(["ID", "Category"])
    for category_id, category in categories.items():
        table.add_row([category_id, category])
    print(table)

# Function to check if a category is registered
def is_category_registered(categories, category_id):
    return category_id in categories

# Function to add an expense and store it in a text file
def add_expense(expenses, amount, category_id, description, filename, categories):
    if not is_category_registered(categories, category_id):
        print("Category ID '{}' is not registered. Please register it first.".format(category_id))
        return False
    expenses.append({"amount": amount, "category_id": category_id, "description": description})
    with open(filename, "a") as file:
        file.write("{},{},{}\n".format(amount, category_id, description))
    return True

# Function to add a crop and store it in a text file
def add_crop(crops, name, planting_date, variety, category_id, filename, categories):
    if not is_category_registered(categories, category_id):
        print("Category ID '{}' is not registered. Please register it first.".format(category_id))
        return False
    crop_id = str(len(crops) + 1)
    crops[crop_id] = {"name": name, "planting_date": planting_date, "variety": variety, "category_id": category_id}
    with open(filename, "a") as file:
        file.write("{},{},{},{},{}\n".format(crop_id, name, planting_date, variety, category_id))
    return True

# Function to load expenses from a text file
def load_expenses(filename):
    expenses = []
    try:
        with open(filename, "r") as file:
            for line in file:
                amount, category_id, description = line.strip().split(',')
                expenses.append({"amount": amount, "category_id": category_id, "description": description})
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        pass
    return expenses

# Function to load crops from a text file
def load_crops(filename):
    crops = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                crop_id, name, planting_date, variety, category_id = line.strip().split(',')
                crops[crop_id] = {"name": name, "planting_date": planting_date, "variety": variety, "category_id": category_id}
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        pass
    return crops

# Function to display all expenses
def display_expenses(expenses, categories):
    table = PrettyTable(["Amount", "Category", "Description"])
    for expense in expenses:
        category = categories.get(expense['category_id'], 'Unknown')
        table.add_row([expense['amount'], category, expense['description']])
    print(table)

# Function to edit an expense
def edit_expense(expenses, amount, category_id, description, filename):
    expense_code = input("Enter the expense code to edit: ")
    for expense in expenses:
        if expense['amount'] == expense_code:
            expense['amount'] = amount
            expense['category_id'] = category_id
            expense['description'] = description
            break
    with open(filename, "w") as file:
        for expense in expenses:
            file.write("{},{},{}\n".format(expense['amount'], expense['category_id'], expense['description']))

# Function to delete an expense
def delete_expense(expenses, filename):
    expense_code = input("Enter the expense code to delete: ")
    for expense in expenses:
        if expense['amount'] == expense_code:
            expenses.remove(expense)
            break
    with open(filename, "w") as file:
        for expense in expenses:
            file.write("{},{},{}\n".format(expense['amount'], expense['category_id'], expense['description']))

# Function to display all crops
def display_crops(crops, categories):
    table = PrettyTable(["ID", "Name", "Planting Date", "Variety", "Category"])
    for crop_id, crop in crops.items():
        category = categories.get(crop['category_id'], 'Unknown')
        table.add_row([crop_id, crop['name'], crop['planting_date'], crop['variety'], category])
    print(table)

# Function to edit a crop
def edit_crop(crops, name, planting_date, variety, category_id, filename):
    for crop_id, crop in crops.items():
        if crop['name'] == name:
            crop['planting_date'] = planting_date
            crop['variety'] = variety
            crop['category_id'] = category_id
            break
    with open(filename, "w") as file:
        for crop_id, crop in crops.items():
            file.write("{},{},{},{},{}\n".format(crop_id, crop['name'], crop['planting_date'], crop['variety'], crop['category_id']))

# Function to delete a crop
def delete_crop(crops, name, filename):
    for crop_id, crop in crops.items():
        if crop['name'] == name:
            del crops[crop_id]
            break
    with open(filename, "w") as file:
        for crop_id, crop in crops.items():
            file.write("{},{},{},{},{}\n".format(crop_id, crop['name'], crop['planting_date'], crop['variety'], crop['category_id']))

# Function to generate a report of expenses categorized by categories
def generate_expense_report(expenses, categories):
    category_totals = {}
    for expense in expenses:
        category_id = expense['category_id']
        category = categories.get(category_id, 'Unknown')
        amount = float(expense['amount'])
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    
    table = PrettyTable(["Category", "Total Expense"])
    total_expenses = 0
    for category, total in category_totals.items():
        table.add_row([category, total])
        total_expenses += total
    
    print(table)
    print("Total expenses: {}".format(total_expenses))
    print("Number of categories: {}".format(len(category_totals)))

# Function to generate a report of crops categorized by categories
def generate_crop_report(crops, categories):
    category_counts = {}
    for crop_id, crop in crops.items():
        category_id = crop['category_id']
        category = categories.get(category_id, 'Unknown')
        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts[category] = 1
    
    table = PrettyTable(["Category", "Number of Crops"])
    total_crops = 0
    for category, count in category_counts.items():
        table.add_row([category, count])
        total_crops += count
    
    print(table)
    print("Total crops: {}".format(total_crops))
    print("Number of categories: {}".format(len(category_counts)))

# Function to login a user
def login(users, username, password):
    for user_id, (uname, pwd) in users.items():
        if uname == username and pwd == password:
            print("Login successful.")
            return True, user_id
    print("Login failed. Please check your username and password.")
    return False, None

# Function to signup a new user
def signup(users, username, password, filename):
    if any(username == user[0] for user in users.values()):
        print("Username already exists. Please choose another username.")
        return False
    else:
        user_id = str(len(users) + 1)
        users[user_id] = (username, password)
        with open(filename, "a") as file:
            file.write("{},{},{}\n".format(user_id, username, password))
        print("User '{}' signed up successfully.".format(username))
        return True, user_id
    
# Function to edit user information
def edit_user(users, user_id, new_username, new_password, filename):
    if user_id not in users:
        print("User ID '{}' does not exist.".format(user_id))
        return False
    users[user_id] = (new_username, new_password)
    with open(filename, "w") as file:
        for uid, (username, password) in users.items():
            file.write("{},{},{}\n".format(uid, username, password))
    print("User information updated successfully.")
    return True

# Function to logout a user
def logout():
    print("Logout successful.")
    return False
