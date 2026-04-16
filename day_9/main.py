from art import logo

print(logo)

dict = {}

print("Welcome to the secret auction program.")
while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    dict[name] = bid
    cont = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    print("\n" * 100)
    if cont == "no":
        break
    
bid_name, max_bid = "", 0
for key in dict:
    if dict[key] > max_bid:
        max_bid = dict[key]
        bid_name = key
        
print(f"The winner is {bid_name} with a bid of ${max_bid}.")


