from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=300)
window.config(padx=30, pady=100)

input = Entry(textvariable=0, width=10)
input.grid(row=0, column=1, padx=10, pady=10)

text_list = ["Miles", "is equal to", "0", "Km"]
labels = [Label(text=txt, font=("Arial", 20, "bold")) for txt in text_list]
labels[0].grid(row=0, column=2)
labels[1].grid(row=1, column=0)
labels[2].grid(row=1, column=1)
labels[3].grid(row=1, column=2)

def calc():
    labels[2].config(text=str(float(input.get()) * 1.60934))

button = Button(text="Calculate", font=("Arial", 20, "bold"), command=calc)
button.grid(row=2, column=1)



window.mainloop()
