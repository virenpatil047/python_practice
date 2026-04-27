import random

# if random.randint(1,2) == 2 :
#     coin = "Tails"
# else :
#     coin = "Heads"
    
# print(coin)

# friends = ["Alice", "Bob", "Charlie", "David",
# "Emanuel"]
# print(friends[random.randint(0,len(friends)-1)])

rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

lst = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(lst[choice])
computer_choice = random.randint(0,2)
print(f"Computer choise : \n{lst[computer_choice]}")

def game():
    if(choice == 0):
        if(computer_choice == 0):
            return 0
        elif(computer_choice == 1):
            return 1
        else:
            return 2
    elif(choice == 1):
        if(computer_choice == 0):
            return 1
        elif(computer_choice == 1):
            return 0
        else:
            return 2
    else:
        if(computer_choice == 0):
            return 1
        elif(computer_choice == 1):
            return 2
        else:
            return 0

if(game()==0):
    print("Game draw !")
elif(game()==1):
    print("You lose")
else:
    print("You win")
