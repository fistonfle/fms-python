# Farm Management System (FMS)

The Farm Management System (FMS) is a command-line application developed in Python to help farmers manage their farm data, including expenses, crops, and user accounts. This README provides an overview of the project and documents its functionalities.

## Overview

The FMS allows farmers to record and manage their farm expenses and crops through a simple command-line interface. Additionally, it provides user authentication functionalities, allowing users to sign up for new accounts and log in to existing accounts.

## Features

- **Signup**: New users can sign up for an account by choosing a unique username and password.
- **Login**: Registered users can log in to their accounts using their credentials.
- **Add Expenses**: Users can add expenses to record their farm-related spending.
- **Add Crops**: Users can add information about the crops they are growing on their farm.
- **View Expenses**: Users can view a list of recorded expenses.
- **View Crops**: Users can view a list of the crops they have added to their farm.

## Usage

1. Ensure you have Python installed on your system.
2. Clone or download this repository.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the command `python main.py` to start the Farm Management System.
5. Follow the on-screen prompts to sign up for a new account or log in to an existing account.
6. After logging in, you can add, view, or manage expenses and crops from the system menu.

## File Structure

- `main.py`: The main Python script containing the application logic.
- `utils.py`: A Python module containing utility functions for user authentication, data storage, and farm operations.
- `users.txt`: Text file storing the registered user accounts (username and password).
- `expenses.txt`: Text file storing the recorded farm expenses.
- `crops.txt`: Text file storing the information about the crops grown on the farm.

## Requirements

- Python 3.x

## Notes

- This is a basic version of the Farm Management System and may be expanded with additional features and improvements in the future.
