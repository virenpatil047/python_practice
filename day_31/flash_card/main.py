from tkinter import *
from pathlib import Path
import pandas as pd
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
BASE = Path(__file__).parent
CARD_FRONT = BASE / "images/card_front.png"
CARD_BACK = BASE / "images/card_back.png"
BASE_FILE = BASE / "data/french_words.csv"
LEARN_FILE = BASE / "data/words_to_learn.csv"
flip_timer = None
french_word = ""
english_word = ""

# ---------------------------- DATA ------------------------------- # 
try:
    df = pd.read_csv(LEARN_FILE)
except FileNotFoundError:
    df = pd.read_csv(BASE_FILE)
finally:
    word_map = {}
    for (index, row) in df.iterrows():
        word_map[row.French] = row.English 

# ---------------------------- NEXT CARD ------------------------------- #    
def next_card(flag):
    if flag == 0:
        global french_word
        french_word = random.choice(list(word_map.keys()))
        global english_word
        english_word = word_map[french_word]
        card.itemconfig(card_img, image=card_front_img)
        card.itemconfig(lang, fill="black", text="French")
        card.itemconfig(word, fill="black", text=french_word)
        
    else:
        card.itemconfig(card_img, image=card_back_img)
        card.itemconfig(lang, fill="white", text="English")
        card.itemconfig(word, fill="white", text=english_word)

# ---------------------------- TIMER ------------------------------- # 
def timer(i):
    next_card(i)
    global flip_timer
    flip_timer = window.after(3000, timer, 1 - i)

def reset_timer():
    window.after_cancel(flip_timer)
    timer(0)

# ---------------------------- WORDS TO LEARN ------------------------------- #
def right():
    del word_map[french_word]
    with open(LEARN_FILE, "w", encoding="utf-8") as f:
        f.write("French,English")
        for (french, english) in word_map.items():
            f.write(f"\n{french},{english}")
    reset_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=CARD_FRONT)
card_back_img = PhotoImage(file=CARD_BACK)
card_img = card.create_image(400, 263, image=card_front_img)
lang = card.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
word = card.create_text(400, 263, text="English", fill="black", font=("Ariel", 60, "bold"))
card.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file=BASE / "images/right.png")
right = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=right)
right.grid(row=1, column=0)

wrong_image = PhotoImage(file=BASE / "images/wrong.png")
wrong = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=reset_timer)
wrong.grid(row=1, column=1)

timer(0)


window.mainloop()
