import pandas as pd
from pathlib import Path

# Dictionary in NATO format.
BASE_PATH = Path(__file__).parent
df = pd.read_csv(BASE_PATH / "nato_phonetic_alphabet.csv")
nato_alpha = {row.letter : row.code for (index, row) in df.iterrows()}
# {"A": "Alfa", "B": "Bravo"}

# List of the phonetic code words from a word that the user inputs.
def nato():
    name = input("Enter name : ").upper()
    try:
        nato_name = {word : nato_alpha[word] for word in name}
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato()
    else:
        print(nato_name)

nato()
