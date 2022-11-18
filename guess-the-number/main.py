#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Check users guess against answer
def check_answer(guess, number, lives):
  """Checks users guess against answer."""
  if guess > number:
    print("Too high.")
    return lives - 1
  elif guess < number:
    print("Too low.") 
    return lives - 1
  else:
    print(f"You got it. The answer was {number}.")

#Prompt user for difficulty level
def set_difficulty():
  """Sets the difficulty level."""
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():   
  # Initialize game
  print(logo)
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
  
  # Select a random number
  number = random.randint(1, 100)
  print(f"Our number is: {number}")
  
  # Ask user to set difficulty
  lives = set_difficulty()

  guess = 0
  while guess != number:
   # Let user guess number 
    print(f"You have {lives} attempts left to guess the number.")
    guess = int(input("Make a guess: "))
  
    lives = check_answer(guess, number)
    if lives == 0:
      print("You've run out of guess, you lose.")
      return
    elif guess != number:
      print("Guess again!")

game() 