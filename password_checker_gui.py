
import tkinter as tk
from tkinter import ttk
import re

def check_strength(event=None):
    password = entry.get()
    score = 0
    tips = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters")

    if re.search(r'[A-Z]', password): score += 1
    else: tips.append("Add uppercase letter")

    if re.search(r'[a-z]', password): score += 1
    else: tips.append("Add lowercase letter")

    if re.search(r'[0-9]', password): score += 1
    else: tips.append("Add a number")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): score += 1
    else: tips.append("Add a special character")

    if score <= 2:
        result_label.config(text="Weak 🔴", fg="red")
    elif score <= 4:
        result_label.config(text="Medium 🟡", fg="orange")
    else:
        result_label.config(text="Strong 🟢", fg="green")

    tips_label.config(text="\n".join(tips) if tips else "Looks good!")

root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("400x300")

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
entry.pack()
entry.bind("<KeyRelease>", check_strength)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=15)

tips_label = tk.Label(root, text="", font=("Arial", 10), justify="left", wraplength=350)
tips_label.pack()

root.mainloop()