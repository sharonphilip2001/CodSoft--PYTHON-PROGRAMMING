import tkinter as tk
from tkinter import messagebox, simpledialog

tasks = []

def update_listbox():
    task_listbox.delete(0, tk.END)
    for t in tasks:
        status = "✅" if t["done"] else "❌"
        task_listbox.insert(tk.END, f"{t['task']} {status}")

def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append({"task": task, "done": False})
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def edit_task():
    try:
        idx = task_listbox.curselection()[0]
        old_task = tasks[idx]["task"]
        new_task = simpledialog.askstring("Edit Task", f"Edit task:", initialvalue=old_task)
        if new_task and new_task.strip():
            tasks[idx]["task"] = new_task.strip()
            update_listbox()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")
    except IndexError:
        messagebox.showwarning("Warning", "Select a task first!")

def mark_done():
    try:
        idx = task_listbox.curselection()[0]
        tasks[idx]["done"] = True
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task first!")

def mark_undone():
    try:
        idx = task_listbox.curselection()[0]
        tasks[idx]["done"] = False
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task first!")

def delete_task():
    try:
        idx = task_listbox.curselection()[0]
        removed = tasks.pop(idx)
        update_listbox()
        messagebox.showinfo("Deleted", f"Deleted task: {removed['task']}")
    except IndexError:
        messagebox.showwarning("Warning", "Select a task first!")

def clear_all():
    global tasks
    tasks = []
    update_listbox()

# --- UI Setup ---
root = tk.Tk()
root.title("To-Do List App")

frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=30)
task_entry.pack(side=tk.LEFT, padx=5)

add_btn = tk.Button(frame, text="➕ Add", command=add_task)
add_btn.pack(side=tk.LEFT)

task_listbox = tk.Listbox(root, width=50, height=12)
task_listbox.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

edit_btn = tk.Button(btn_frame, text="✏️ Edit", width=12, command=edit_task)
edit_btn.grid(row=0, column=0, padx=5, pady=5)

done_btn = tk.Button(btn_frame, text="✅ Mark Done", width=12, command=mark_done)
done_btn.grid(row=0, column=1, padx=5, pady=5)

undone_btn = tk.Button(btn_frame, text="❌ Mark Undone", width=12, command=mark_undone)
undone_btn.grid(row=0, column=2, padx=5, pady=5)

delete_btn = tk.Button(btn_frame, text="🗑️ Delete", width=12, command=delete_task)
delete_btn.grid(row=1, column=0, padx=5, pady=5)

clear_btn = tk.Button(btn_frame, text="🧹 Clear All", width=12, command=clear_all)
clear_btn.grid(row=1, column=1, padx=5, pady=5)

exit_btn = tk.Button(btn_frame, text="🚪 Exit", width=12, command=root.quit)
exit_btn.grid(row=1, column=2, padx=5, pady=5)

root.mainloop()
