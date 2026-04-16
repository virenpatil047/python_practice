# score = [100, 90, 20, 200, 40, 10, 2, 49, 90]
# minn=score[0]
# for i in score:
#     if i < minn:
#         minn=i
# print(minn)

# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)

import random

letters = [
    'a','b','c','d','e','f','g','h','i','j','k',
    'l','m','n','o','p','q','r','s','t','u',
    'v','w','x','y','z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
n_numbers = int(input(f"How many numbers would you like?\n"))

def rand_func(lst, n):
    s = ""
    for i in range(0,n):
        s += random.choice(lst)
    return s

pwd = rand_func(letters, nr_letters) + rand_func(symbols, nr_symbols) + rand_func(numbers, n_numbers)

lst = list(pwd)
random.shuffle(lst)
h_pwd = ""
for c in lst:
    h_pwd += c

print(f"Final Password : {pwd} ::: {h_pwd}")