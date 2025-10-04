import tkinter as tk
from tkinter import ttk

def on_click(button_text):
    current_text = entry_var.get()
    
    if button_text == "C":  # Clear
        entry_var.set("")
    elif button_text == "=":  # Evaluate
        try:
            result = str(eval(current_text))
            entry_var.set(result)
        except:
            entry_var.set("Error")
    else:
        entry_var.set(current_text + button_text)

# GUI Setup
root = tk.Tk()
root.title("Modern Calculator 🧮")
root.geometry("320x450")
root.configure(bg="#2c3e50")

style = ttk.Style()
style.configure("TButton", font=("Arial", 14, "bold"), padding=8)

# Entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief="ridge", justify="right")
entry.pack(fill="both", padx=10, pady=15, ipady=10)

# Buttons Layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

# Create button grid
frame = tk.Frame(root, bg="#2c3e50")
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame, bg="#2c3e50")
    row_frame.pack(expand=True, fill="both")
    for btn in row:
        action = lambda x=btn: on_click(x)
        b = tk.Button(row_frame, text=btn, font=("Arial", 16, "bold"),
                      bg="#34495e", fg="white", activebackground="#1abc9c",
                      activeforeground="white", relief="flat",
                      height=2, width=6, command=action)
        b.pack(side="left", expand=True, fill="both", padx=3, pady=3)

root.mainloop()
