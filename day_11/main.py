import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    
    score = {
        "player" : [], 
        "computer" : []
        }
    player_sum, computer_sum = 0, 0
    cont = ""
    
    cont = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if cont != "y":
        return
    
    def choose():
        """Deal Cards."""
        return random.choice(cards)
    
    def get_another_card(hand):
        score[hand].append(choose())
    
    def check_sum(lst):
        """Check for ACE."""
        total = sum(lst)
        if 11 in lst and total > 21:
            for i in range(0,lst.count(11)):
                lst[lst.index(11)] = 1
                total -= 10
                if total <= 21:
                    return total
        return total
    
    def show():
        print(f"\tYour cards: {score["player"]}, current score: {player_sum}")
        print(f"\tComputer's first card: {score["computer"][0]}")
        
    def final_hand():
        print(f"\tYour final hand: {score["player"]}, final score: {player_sum}")
        print(f"\tComputer's final hand: {score["computer"]}, final score: {computer_sum}")
        
    get_another_card("player")
    get_another_card("player")
    get_another_card("computer")
    get_another_card("computer")
    
    player_sum = check_sum(score["player"])
    computer_sum = check_sum(score["computer"])
    
    show()
    
    cont = input("Type 'y' to get another card, type 'n' to pass: ")
    
    while cont == "y":
        get_another_card("player")
        player_sum = check_sum(score["player"])
        if player_sum > 21:
            final_hand()
            print("You went over. You lose 😭")
        show()
        cont = input("Type 'y' to get another card, type 'n' to pass: ")
    
    while not sum(score["computer"]) > 16:
        get_another_card("computer")
        computer_sum = check_sum(score["computer"])
    
    if computer_sum > 21:
        final_hand()
        print("Opponent went over. You win 😁")
    elif 21 - computer_sum > 21 - player_sum:
        final_hand()
        if 11 in score["player"]:
            print("Win with a Blackjack 😎")
        else:
            print("You win 😃")
    elif 21 - computer_sum == 21 - player_sum:
        final_hand()
        print("Draw !")
    else:
        final_hand()
        if 11 in score["computer"]:
            print("Lose, opponent has Blackjack 😱")
        else:
            print("You lose 😤")
    
    blackjack()

print(art.logo)
blackjack()
        
