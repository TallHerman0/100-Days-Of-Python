from tkinter import *
from tkinter import messagebox
import random
import json

WHITE = "#FFFFFF"
FONT_NAME = "Arial"

lowercase_alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
uppercase_alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    listss = (lowercase_alphabet, uppercase_alphabet, numbers, chars)
    global password
    password = ""

    while len(password) < 14:
        choice = random.choice(listss)
        if choice == numbers:
            string = str(random.choice(choice))
            password += string
        else:
            password += random.choice(choice)

    #print(password)
    text_var.set(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get(),
            }    
        }
    if len(password_entry.get()) == 0 or len(email_entry.get()) == 0:
        messagebox.showerror("Error", "You can't leave any field empty", icon="error")
    else:
        try:
            with open('passwords.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:        
                with open('passwords.json', 'w') as f:
                    json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open('passwords.json', 'w') as f:
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

        messagebox.showinfo("Success", "Your information has been saved", icon="info")

# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():

    web = website_entry.get()
    try:
        with open("passwords.json", "r") as f:
            passwords = json.load(f)
        messagebox.showinfo(f"{web}", f"Website: {passwords[web]["email"]}\nPassword: {passwords[web]["password"]}", icon="info")
    except KeyError:
        messagebox.showerror("Error", f"{web} is not part of the websites saved on the app", icon="error")
    except FileNotFoundError:
        messagebox.showerror("Error", "There is no file of saved passwords yet!!!", icon="error")
    #print(passwords[web]["password"])
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

# ----------------- SETUP -----------------
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)           # more breathing room around edges

# Give columns weight so they expand nicely when window is resized
window.columnconfigure(0, weight=0)       # labels column - minimal width
window.columnconfigure(1, weight=1)       # entry column - takes most space
window.columnconfigure(2, weight=0)       # generate button column - just enough

# ----------------- CANVAS (LOGO) -----------------
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3, pady=(0, 30))   # centered on top

# ----------------- LABELS & ENTRIES -----------------
# Website
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e", pady=5, padx=(0, 10))

website_entry = Entry(width=40)                     # wider for comfort
website_entry.grid(row=1, column=1, sticky="ew", pady=5)
website_entry.focus()                               # start here
website = website_entry.get()

search_btn = Button(text="Search Website", command=search_website)
search_btn.grid(row=1, column=2, sticky="ew", pady=5)

# Email / Username
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e", pady=5, padx=(0, 10))

email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew", pady=5)
email_entry.insert(0, "kbokaba3@gmail.com")

# Password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e", pady=5, padx=(0, 10))

text_var = StringVar(value = "")
password_entry = Entry(width=22, textvariable=text_var)                    # shorter to fit button
password_entry.grid(row=3, column=1, sticky="ew", pady=5, padx=(0, 8))
password = password_entry.get()

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(row=3, column=2, sticky="ew", pady=5)

# ----------------- ADD BUTTON -----------------
add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2, pady=(20, 0), sticky="ew")

# ----------------- START -----------------
window.mainloop()