import tkinter as tk

root = tk.Tk()
root.title("True / False - Grid layout")
root.geometry("400x280")
root.configure(bg="#0066cc")          # medium blue background

# Configure the root grid so we can place score in top-right
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)   # main content gets most space

# ── Score label ── top-right corner ────────────────────────────────
score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Segoe UI", 14, "bold"),
    bg="#0066cc",
    fg="white",
    padx=15,
    pady=8
)
score_label.grid(
    row=0,
    column=0,
    sticky="ne",           # north-east = top-right
    padx=10,
    pady=10
)

# ── Main content frame (centered) ─────────────────────────────────
main_frame = tk.Frame(root, bg="#0066cc")
main_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

# Let the main_frame expand
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=1)

# Textbox
textbox = tk.Entry(
    main_frame,
    font=("Segoe UI", 15),
    width=26,
    justify="center"
)
textbox.grid(
    row=0,
    column=0,
    padx=20,
    pady=(40, 30),
    sticky="ew"
)

# Buttons container
buttons_frame = tk.Frame(main_frame, bg="#0066cc")
buttons_frame.grid(row=1, column=0, pady=20, sticky="n")

btn_true = tk.Button(
    buttons_frame,
    text="True",
    font=("Segoe UI", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    width=10,
    relief="flat",
    padx=12,
    pady=10,
    command=lambda: print("Clicked: True")
)
btn_true.grid(row=0, column=0, padx=30)

btn_false = tk.Button(
    buttons_frame,
    text="False",
    font=("Segoe UI", 14, "bold"),
    bg="#F44336",
    fg="white",
    width=10,
    relief="flat",
    padx=12,
    pady=10,
    command=lambda: print("Clicked: False")
)
btn_false.grid(row=0, column=1, padx=30)

root.mainloop()