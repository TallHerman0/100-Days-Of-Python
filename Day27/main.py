import tkinter as tk

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

def button_clicked():
    my_label.config(text=f"{input.get()}")

my_label = tk.Label(text="I am a label", font=("Arial", 20, "italic"))
my_label.grid(column=0, row=0)
my_label["text"] = "New Text"

#Buttons
button = tk.Button(text="Submit", command=button_clicked)
button.grid(column=1, row=1)

button2 = tk.Button(text="New Button")
button2.grid(column=2, row=0)
#Entry
input = tk.Entry(width=10)
input.grid(column=4, row=4)

window.mainloop()