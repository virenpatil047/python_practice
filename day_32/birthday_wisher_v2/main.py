import pandas as pd
import random, smtplib
from pathlib import Path
from datetime import datetime as dt

BASE_PATH = Path(__file__).parent

sender_email = "wren@gmail.com"
sender_pwd = "test"

curr_day = dt.now().day
curr_month = dt.now().month

df = pd.read_csv(BASE_PATH / "birthdays.csv")
df = df[(df["month"] == curr_month) & (df["day"] == curr_day)]

def send_mail(email, content):
    reciever_email = email
    letter = ""
    for line in content:
        letter += line + "\n"
    wishes = f"Subject: Birthday Wishes !!\n\n{letter}"
    with smtplib.SMTP("smtp.gmail.com", 587) as conn:
        conn.starttls()
        conn.login(sender_email, sender_pwd)
        conn.sendmail(
            from_addr=sender_email,
            to_addrs=reciever_email,
            msg=wishes
        )

if not df.empty:
    for index, row in df.iterrows():
        letter = "letter_" + str(random.randint(1, 3)) + ".txt"
        with open(BASE_PATH / "letter_templates" / letter) as f:
            content = f.readlines()
            for i in range(0, len(content)):
                if "[NAME]" in content[i]:
                    content[i] = content[i].replace("[NAME]", row["name"])
                content[i] = content[i].strip()
            send_mail(row.email, content)
