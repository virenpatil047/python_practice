import os
from pathlib import Path

BASE_DIR = Path(__file__).parent
NAME = BASE_DIR / "Input" / "Names" / "invited_names.txt"
LETTER = BASE_DIR / "Input" / "Letters" / "starting_letter.txt"
WRITE_LETTER = BASE_DIR / "Output" / "ReadyToSend"

with open(NAME) as names_file:
    names = names_file.readlines()

for i in range(0, len(names)):
    names[i] = names[i].strip()
    
with open(LETTER) as letter:
    letter_name = letter.readline()
    letter_content = letter.readlines()[1:]

for name in names:
    with open(WRITE_LETTER / f"letter_for_{name}.txt", "w") as write_letter:
        write_letter.write(letter_name.replace("[name]", name))
        write_letter.write("\n")
        write_letter.writelines(letter_content)
