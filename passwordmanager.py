# This is a simple password manager that allows you to store and retrieve passwords securely.
# It uses base64 encoding for encryption and decryption.

#copyright (c) 2025 by Peter Maina

# The passwords are stored in a JSON file, and the user can add or retrieve passwords using a simple command-line interface.

import json
import base64
import getpass
import os

PASSWORD_FILE = "passwords.json"

# Encrypt & Decrypt Functions
def encrypt(text):
    return base64.b64encode(text.encode()).decode()

def decrypt(text):
    return base64.b64decode(text.encode()).decode()

# Load Passwords
def load_passwords():
    if not os.path.exists(PASSWORD_FILE):
        return {}
    with open(PASSWORD_FILE, "r") as file:
        return json.load(file)

# Save Passwords
def save_passwords(passwords):
    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file, indent=4)

# Add a New Password
def add_password():
    site = input("Enter site/app name: ")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    
    passwords = load_passwords()
    passwords[site] = {"username": username, "password": encrypt(password)}
    
    save_passwords(passwords)
    print("✅ Password saved successfully!")

# Retrieve a Password
def get_password():
    site = input("Enter site/app name to retrieve: ")
    passwords = load_passwords()
    
    if site in passwords:
        username = passwords[site]["username"]
        password = decrypt(passwords[site]["password"])
        print(f"🔑 Username: {username}\n🔓 Password: {password}")
    else:
        print("❌ No password found for this site.")

# Main Menu
def main():
    while True:
        print("\n🔐 Simple Password Manager 🔐")
        print("1️⃣ Add a password")
        print("2️⃣ Retrieve a password")
        print("3️⃣ Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
