from tkinter import *
from pathlib import Path

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
BASE = Path(__file__).parent
CARD_FRONT = BASE / "images/card_front.png"
CARD_BACK = BASE / "images/card_back.png"

# ---------------------------- TIMER RESET ------------------------------- # 


# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=CARD_FRONT)
card.create_image(100, 112, image=card_front_img)
lang = card.create_text(400, 150, text="French", fill="white", font=("Ariel", 40, "italic"))
word = card.create_text(400, 150, text="trouve", fill="white", font=("Ariel", 60, "bold"))
card.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file=BASE / "images/right.png")
right = Button(image=right_image, highlightthickness=0)
right.grid(row=1, column=1)

wrong_image = PhotoImage(file=BASE / "images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0)
wrong.grid(row=1, column=2)


window.mainloop()
