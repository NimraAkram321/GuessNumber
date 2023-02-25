#Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo;
import random


#hardCodedText
print(logo)
print("Welcome to the number Guessing Game!")
# Allow the player to submit a guess for a number between 1 and 100.
print("I'm thinking of a number between 1 and 100")
number=random.randint(1,100)

attempts=0
gameType=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if gameType == "easy":
  attempts=10
else:
  attempts=5
#decrement function of attempts  
def attemptsCal():
  if attempts > 0:
    return attempts -1
  else:
    return 0
condition=False    
while not condition:
  print(f"You have {attempts} attempts remaining to guess the number.")
  guessNum=int(input("Make a guess: "))
  
  if guessNum > number:
    print("To high.")
  
  elif guessNum < number:
    print("To low")
  else:
    print("You win!!! :D")
    condition =True
  attempts=attemptsCal()
  if attempts != 0 and not condition :
    print("Guess again")
  elif not condition :
    print("You lose!")
    condition =True
