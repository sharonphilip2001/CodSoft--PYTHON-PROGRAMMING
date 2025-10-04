import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------- Password Generator ---------- #
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Invalid Length", "Password length must be at least 4.")
            return

        characters = ""
        groups = []

        if var_letters.get():
            characters += string.ascii_letters
            groups.append(string.ascii_letters)
        if var_digits.get():
            characters += string.digits
            groups.append(string.digits)
        if var_symbols.get():
            characters += string.punctuation
            groups.append(string.punctuation)

        if not characters:
            messagebox.showwarning("No Options", "Please select at least one character type.")
            return

        # Build password
        password = []
        if var_strict.get():
            for g in groups:
                password.append(random.choice(g))

        while len(password) < length:
            password.append(random.choice(characters))

        random.shuffle(password)
        password = "".join(password)

        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)

        # Show strength
        strength_label.config(text="Strength: " + check_strength(password))

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# ---------- Strength Checker ---------- #
def check_strength(password):
    length = len(password)
    has_letters = any(c.isalpha() for c in password)
    has_digits = any(c.isdigit() for c in password)
    has_symbols = any(c in string.punctuation for c in password)

    score = sum([has_letters, has_digits, has_symbols])

    if length < 6 or score < 2:
        return "Weak ❌"
    elif length < 10:
        return "Medium ⚠️"
    else:
        return "Strong ✅"

# ---------- Copy to Clipboard ---------- #
def copy_password():
    pwd = result_entry.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# ---------- GUI Setup ---------- #
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("420x320")
root.resizable(False, False)

# Password length
tk.Label(root, text="Password Length:", font=("Arial", 12)).pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 12), justify="center")
length_entry.insert(0, "12")  # default length
length_entry.pack(pady=5)

# Options
var_letters = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)
var_strict = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=var_letters).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Digits", variable=var_digits).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Strict Mode (include all selected types)", variable=var_strict).pack(anchor="w", padx=50)

# Buttons
tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password).pack(pady=10)

result_entry = tk.Entry(root, font=("Arial", 12), justify="center", width=30)
result_entry.pack(pady=5)

strength_label = tk.Label(root, text="Strength: ", font=("Arial", 12))
strength_label.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), command=copy_password).pack(pady=10)

root.mainloop()
