import tkinter as tk

window = tk.Tk()
window.title("Kilometers to Miles Converter")
window.minsize(width=200, height=100)
window.config(padx=50, pady=50)

#functions
def calculate_answer():
    label3.config(text=f"{round(float(input1.get())*0.621371, 2)}")

#inupts
input1 = tk.Entry(width=12)
input1.grid(column=4, row=3)

#Labels
label1 = tk.Label(text="KMs", font=("Arial", 10))
label1.grid(column=5, row=3)
label1.config(padx=10)

label2 = tk.Label(text="is equal to", font=("Arial", 10))
label2.grid(column=3, row=4)

label3 = tk.Label(text="0", font=("Arial", 10))
label3.grid(column=4, row=4)

label4 = tk.Label(text="M", font=("Arial", 10))
label4.grid(column=5, row=4)

#Buttons
button = tk.Button(text="Calculate", command=calculate_answer)
button.grid(column=4, row=5)

window.mainloop()