#Number Guessing Game

from random import randint

HARD_GUESS = 5
EASY_GUESS = 10

def check_answer(guess, answer, turns):

  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
    print("Too Low")
    return turns - 1
  elif guess == answer:
    print(f"You got it. The answer was {answer}!")

def set_difficulty():
  level = input("choose difficulty. Hard or easy? ")
  if level == "hard":
    return HARD_GUESS
  else:
    return EASY_GUESS


def game():

  from art import logo
  print(logo)

  print("Welcome to number guessing game.")

  answer = randint(1, 100)

  turns = set_difficulty() 

  guess = 0
 
  while guess != answer:

    print(f"You have {turns} turns left to guess the number.")
    guess = int(input("make a guess "))
    turns = check_answer(guess, answer, turns)

    if turns == 0:
      print("You ran out of guesses!")
      print(f"The answer is {answer}.")
      return
    elif guess != answer:
      print("Guess again")


game()

