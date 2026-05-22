from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json
from pathlib import Path

BASE = Path(__file__).parent
LOGO = BASE / "logo.png"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    
    entry[2].delete(0, END)
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    
    entry[2].insert(0, password)
    
    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    web = entry[0].get()
    u_id = entry[1].get()
    pwd = entry[2].get()
    new_data = {
        web : {
            "username": u_id,
            "password" : pwd
        }
    }
    
    if not all([web, u_id, pwd]):
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty !")
        return
    
    is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered : \nEmail : {u_id}"
                                                        f"\nPassword : {pwd} \nIs it ok to save ?")
    
    if not is_ok:
        return
    
    try:
        with open(BASE / "data.json", 'r') as f:
            data = json.load(f)
            data.update(new_data)
    except FileNotFoundError:
        with open(BASE / "data.json", 'w') as f:
            json.dump(new_data, f, indent=4)
    else:    
        with open(BASE / "data.json", 'w') as f:
            json.dump(data, f, indent=4)
    finally:
        with open(BASE / "data.txt", 'a') as f:
            f.write(f"{web} | {u_id} | {pwd}\n")
        entry[0].delete(0, END)
        entry[2].delete(0, END)


# ---------------------------- SEARCH ------------------------------- #
def find_password():
    srch.config(bg="lightblue")
    web = entry[0].get()
    try:
        with open(BASE / "data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title=web, message="No data file found !")
    else:
        if web not in data:
            messagebox.showinfo(title=web, message="No details for the website exists !")
        else:
            u_id = data[web]["username"]
            pwd = data[web]["password"]
            messagebox.showinfo(title=web, message=f"Email : {u_id}"
                                                f"\nPassword : {pwd}")
    finally:
        srch.config(bg="white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file=LOGO)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

label_info = {
    "Website : " : (1,0),
    "Email/Username : " : (2,0),
    "Password : " : (3,0)
}

label = []
for (label_text, pos) in label_info.items():
    create_label = Label(text=label_text)
    create_label.grid(row=pos[0], column=pos[1])
    label.append(create_label)

entry_info = {
    (1,1) : 34,
    (2,1) : 52,
    (3,1) : 34
}

entry = []
for (pos, entry_width) in entry_info.items():
    input = Entry(width=entry_width)
    input.grid(row=pos[0], column=pos[1], columnspan=2 if entry_width >= 35 else 1)
    entry.append(input)

entry[0].focus()
entry[1].insert(0, "virenpatil047@gmail.com")

gen_pwd = Button(text="Generate Password", command=generate_pwd)
gen_pwd.grid(row=3, column=2)

srch = Button(text="Search", width=14, command=find_password)
srch.grid(row=1, column=2)

add = Button(text="Add", width=44, command=add_to_file)
add.grid(row=4, column=1, columnspan=2)


window.mainloop()
