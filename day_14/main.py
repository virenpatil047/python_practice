import random
from game_data import data
from art import logo, vs

score = 0

def check_answer(fol1, fol2, ch):
    """Check answer for the count of followers."""
    if fol1 > fol2:
        return ch == "a"
    else:
        ch == "b"

compare_a = random.choice(data)

while True:

    print(logo)
    
    if score != 0:
        print(f"You're right! Current score: {score}.")
    
    print(f"Compare A: {compare_a["name"]}, a {compare_a["description"]}, from {compare_a["country"]}.")
    
    print(vs)
    
    compare_b = random.choice(data)
    while compare_b == compare_a:
        compare_b = random.choice(data)
    
    print(f"Against B: {compare_b["name"]}, a {compare_b["description"]}, from {compare_b["country"]}.")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    while answer != "a" and answer != "b":
        print("Invalid choice, try again !")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    if check_answer(compare_a["follower_count"], compare_b["follower_count"], answer):
        score += 1
        compare_a = compare_b
        print("\n" * 100)
        
    else:
        print("\n" * 100)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break
