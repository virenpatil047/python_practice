# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# if(size == "S"):
#     price = 15
# elif(size == "M"):
#     price = 20
# else:
#     price = 25

# if(pepperoni == "Y"):
#     if(size == "S"):
#         price+=1
#     else:
#         price+=3

# if(extra_cheese == "Y"):
#     price+=1

# print(f"Your final bill is : {price}.")

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to treasure island.\n
        "Your mission is to find the treasure.")
choice = input(("Will you go left or right ? "))
if(choice.casefold() == "Right".casefold()):
    print("Game Over.")
    exit()
choice = input(("Will you swim or wait ? "))
if(choice.casefold() == "swim".casefold()):
    print("Game Over.")
    exit()
choice = input(("which door will you select ?? Blue, Red or Yellow ? "))
if(choice.casefold() == "Red".casefold() or choice.casefold() == "Blue".casefold()):
    print("Game Over. ")
    exit()
print("You Win !")
