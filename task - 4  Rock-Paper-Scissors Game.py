import tkinter as tk
from tkinter import messagebox
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Global variables
user_score = 0
computer_score = 0
rounds_to_win = 3  # Default (Best of 3)


def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    # Determine winner
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    # Update labels
    user_label.config(text=f"Your Choice: {user_choice}")
    computer_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=result, fg="green" if "Win" in result else "red" if "Lose" in result else "blue")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

    # Update history
    history_listbox.insert(tk.END, f"You: {user_choice} | Computer: {computer_choice} -> {result}")

    # Check if someone won the match
    if user_score == rounds_to_win or computer_score == rounds_to_win:
        winner = "You won the match! 🎉" if user_score > computer_score else "Computer won the match! 🤖"
        messagebox.showinfo("Game Over", winner)
        ask_restart()


def ask_restart():
    """Ask player if they want to restart after match ends"""
    global user_score, computer_score
    play_again = messagebox.askyesno("Play Again", "Do you want to start a new match?")
    if play_again:
        reset_game()
    else:
        root.destroy()


def reset_game():
    """Reset everything"""
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_label.config(text="Your Choice: ")
    computer_label.config(text="Computer's Choice: ")
    result_label.config(text="")
    score_label.config(text="Score - You: 0 | Computer: 0")
    history_listbox.delete(0, tk.END)


def set_mode(rounds):
    """Set best of mode (3 or 5)"""
    global rounds_to_win
    rounds_to_win = rounds
    messagebox.showinfo("Mode Selected", f"Game mode set to Best of {rounds*2 - 1}!")


# GUI Setup
root = tk.Tk()
root.title("Rock-Paper-Scissors Advanced")
root.geometry("500x500")
root.config(bg="#e6f7ff")

# Title
title_label = tk.Label(root, text="Rock - Paper - Scissors", font=("Arial", 20, "bold"), bg="#e6f7ff", fg="#003366")
title_label.pack(pady=10)

# Mode selection
mode_frame = tk.Frame(root, bg="#e6f7ff")
mode_frame.pack(pady=5)
tk.Label(mode_frame, text="Select Mode:", font=("Arial", 12, "bold"), bg="#e6f7ff").pack(side=tk.LEFT)
tk.Button(mode_frame, text="Best of 3", command=lambda: set_mode(2), bg="#0099cc", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(mode_frame, text="Best of 5", command=lambda: set_mode(3), bg="#0099cc", fg="white").pack(side=tk.LEFT, padx=5)

# Buttons
frame = tk.Frame(root, bg="#e6f7ff")
frame.pack(pady=10)

rock_btn = tk.Button(frame, text="🪨 Rock", width=12, height=2, command=lambda: play("Rock"), bg="#ffcc99")
paper_btn = tk.Button(frame, text="📄 Paper", width=12, height=2, command=lambda: play("Paper"), bg="#ccffcc")
scissors_btn = tk.Button(frame, text="✂️ Scissors", width=12, height=2, command=lambda: play("Scissors"), bg="#ffcccc")

rock_btn.grid(row=0, column=0, padx=10, pady=10)
paper_btn.grid(row=0, column=1, padx=10, pady=10)
scissors_btn.grid(row=0, column=2, padx=10, pady=10)

# Labels
user_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12), bg="#e6f7ff")
user_label.pack()
computer_label = tk.Label(root, text="Computer's Choice: ", font=("Arial", 12), bg="#e6f7ff")
computer_label.pack()
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#e6f7ff")
result_label.pack(pady=5)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12), bg="#e6f7ff")
score_label.pack()

# History box
history_frame = tk.Frame(root, bg="#e6f7ff")
history_frame.pack(pady=10)
tk.Label(history_frame, text="Game History:", font=("Arial", 12, "bold"), bg="#e6f7ff").pack()
history_listbox = tk.Listbox(history_frame, width=50, height=8)
history_listbox.pack()

# Reset button
reset_btn = tk.Button(root, text="Reset Game", command=reset_game, bg="red", fg="white")
reset_btn.pack(pady=10)

root.mainloop()
