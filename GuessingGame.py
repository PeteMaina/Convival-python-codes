
# Guessing game created in python
# Email : peterwahomemaina003@gmail.com | Whatsapp : +254794797796

import random

def number_guessing_game():
  """A simple number guessing game."""
  secret_number = random.randint(1, 100)
  attempts = 0

  print("I'm thinking of a number between 1 and 100.")

  while True:
    try:
      guess = int(input("Take a guess: "))
      attempts += 1

      if guess < secret_number:
        print("Too low!")
      elif guess > secret_number:
        print("Too high!")
      else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
    except ValueError:
      print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  number_guessing_game()