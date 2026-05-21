# def add(*nums):
#     sum = 0
#     for n in nums:
#         sum += n
#     return sum

# print(add(1, 2, 3))
# print(add(1, 2, 3, 4, 5, 9, 10))

from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Laber
label = Label(text="I am a label.", font=("Arial", 24, "bold"))
# label.pack(side="left")
label.grid(row=0, column=0)
label.config(padx=50, pady=50)

# Changing label 
label["text"] = "New text."
label.config(text="Second new text.")

def click():
    label.config(text=input.get())

# Button
button = Button(text="Click me", command=click)
button.grid(row=1, column=1)

new_button = Button(text="New button")
new_button.grid(row=0, column=2)

# Entry
input = Entry(width=10)
input.grid(row=2, column=3)


window.mainloop()