import random
from art import logo

HARD = 10
EASY = 5

def play_guess_num(chances, number):
    while chances > 0:
        print(f"You have {chances} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")
        else:
            print(f"You got it! The answer was {number}.")
            return
        chances -= 1
    print("You've run out of guesses. You lose.")
    
def start_game():
    print("I'm thinking of a number between 1 and 100.")
        
    number = random.randint(1, 100)
    
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    if level == "easy":
        play_guess_num(EASY, number)
    else:
         play_guess_num(HARD, number)

print(logo)
print("Welcome to the Number Guessing Game ! ")
start_game()
while input("Start a new game ? Yes or No ? : ").lower() == "yes":
    print("\n" * 100)
    start_game()