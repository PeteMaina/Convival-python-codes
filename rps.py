
# Rock, Paper, Scissors created in python
# Email : peterwahomemaina003@gmail.com | Whatsapp : +254794797796


import random

def get_computer_choice():
  """Generates a random choice for the computer."""
  choices = ["rock", "paper", "scissors"]
  return random.choice(choices)

def determine_winner(user_choice, computer_choice):
  """Determines the winner of the game."""
  if user_choice == computer_choice:
    return "It's a tie!"

  if is_win(user_choice, computer_choice):
    return "You won!"

  return "You lost!"

def is_win(player, opponent):
  """Returns True if player wins."""
  # Using a dictionary to represent winning conditions
  win_conditions = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
  }
  return win_conditions[player] == opponent

def play():
  """Plays a single round of Rock-Paper-Scissors."""
  user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
  computer_choice = get_computer_choice()
  print(f"You chose {user_choice}, computer chose {computer_choice}.")
  result = determine_winner(user_choice, computer_choice)
  print(result)

if __name__ == "__main__":
  play()
