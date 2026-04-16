import random

word_list = ["aardvark", "baboon", "camel"]
HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
lives = 6

rand_word = random.choice(word_list)
print(rand_word)

placeholder = []
def display():
    for s in placeholder:
        print(s, end="")
    print()
for s in rand_word:
    placeholder.append("_")
display()
live_cnt = 0

def check():
    flag = False
    for i in range(0, len(rand_word)):
        if rand_word[i] == guess:
            placeholder[i] = guess
        if placeholder[i] == "_":
            flag = True
    return flag

game_over = True
while game_over and lives >= 0 :
    guess = input("Guess a letter : ").lower()
    if guess in placeholder: 
        print(HANGMANPICS[live_cnt])
        print("Already Guessed !")
        continue
    game_over = check()
    display()
    if guess not in placeholder:
        live_cnt += 1
        if live_cnt >= 6:
            game_over = False
            print(HANGMANPICS[live_cnt])
            print("You Lose !")
        else:
            print(HANGMANPICS[live_cnt])
    else:
        print(HANGMANPICS[live_cnt])

if not live_cnt >= 6:
    print("You Win !")
