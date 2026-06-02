import smtplib, random
from datetime import datetime as dt
from pathlib import Path

sender_email = "wren@gmail.com"
sender_pwd = "test"
reciever_email = "test@yahoo.com"
base_path = Path(__file__).parent

def send_mail():
    with open(base_path / "quotes.txt") as f:
        lines = f.readlines()
        quote = random.choice(lines)
    content = f"Subject: Motivational Quote\n\n{quote}"
    with smtplib.SMTP("smtp.gmail.com", 587) as conn:
        conn.starttls()
        conn.login(sender_email, sender_pwd)
        conn.sendmail(
            from_addr=sender_email,
            to_addrs=reciever_email,
            msg=content
        )

today = dt.now()
day = today.strftime("%a")
weekend = ["Sat", "Sun"]

if day not in weekend:
    send_mail()
