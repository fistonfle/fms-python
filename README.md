# Farm Management System (FMS)

The Farm Management System (FMS) is a command-line application developed in Python to help farmers manage their farm data, including expenses, crops, and user accounts. This README provides an overview of the project and documents the signup, login, and user data storage functionalities.

## Overview

The FMS allows farmers to record and manage their expenses and crops through a simple command-line interface. Additionally, it provides user authentication functionalities, allowing users to sign up for new accounts and log in to existing accounts.

## Signup

To sign up for a new account, users can choose a username and password. The signup process ensures that the chosen username is unique. Upon successful signup, the user's account information is stored securely in a text file.

## Login

Registered users can log in to their accounts using their username and password. The login process verifies the provided credentials against the stored user data. Upon successful login, users are granted access to the system menu to manage their farm data.

## User Data Storage

User account information, including usernames and passwords, is stored securely in a text file. The system ensures data integrity and confidentiality by encrypting passwords before storing them. The user data storage mechanism allows for seamless user authentication and management.

## Usage

1. Ensure you have Python installed on your system.
2. Clone or download this repository.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the command `python main.py` to start the Farm Management System.
5. Follow the on-screen prompts to sign up for a new account or log in to an existing account.

## File Structure

- `main.py`: The main Python script containing the application logic.
- `utils.py`: A Python module containing utility functions for user authentication and data storage.
- `users.txt`: Text file storing the registered user accounts (username and password).

## Requirements

- Python 3.x

## Notes

- This is a basic version of the Farm Management System and may be expanded with additional features and improvements in the future.
- For enhanced security, consider implementing password hashing and salting mechanisms.
