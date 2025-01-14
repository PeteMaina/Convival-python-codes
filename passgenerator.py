# Ever wanted to generate strong untraceable passwords
# This code allows you to do exactly that
# Email : peterwahomemaina003@gmail.com | Whatsapp : +254794797796

import random
import time
import ipywidgets as widgets
from IPython.display import display, clear_output # Import clear_output
from IPython import get_ipython

# Function to generate the password
def generate_password():
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '1234567890'
    symbols = '!@#$%^&*/?'

    use_for = lower_case + upper_case + numbers + symbols
    length_for_pass = 10

    password = "".join(random.sample(use_for, length_for_pass))
    return password

# Function to handle button click and copy to clipboard
def on_button_click(b):
    password = generate_password()
    print(f"Generated Password: {password}")

    def print_for_seconds(text, seconds):
        time.sleep(seconds)  # Wait for the specified number of seconds
        clear_output(wait=True)  # Clear the output # Indented this line


    print_for_seconds("Password copied to clipboard!", 2) #Removed this line from inside the function


# Create a button
button = widgets.Button(description="Generate New Password")
button.on_click(on_button_click)

# Display the button
display(button)