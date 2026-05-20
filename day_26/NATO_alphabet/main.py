import pandas as pd
from pathlib import Path

#dictionary in NATO format:
BASE_PATH = Path(__file__).parent
df = pd.read_csv(BASE_PATH / "nato_phonetic_alphabet.csv")
nato_alpha = {row.letter : row.code for (index, row) in df.iterrows()}
# {"A": "Alfa", "B": "Bravo"}

#list of the phonetic code words from a word that the user inputs.
name = input("Enter name : ")
nato_name = {word.upper() : nato_alpha[word.upper()] for word in name}
print(nato_name)
