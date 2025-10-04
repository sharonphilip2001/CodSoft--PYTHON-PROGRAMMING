import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

# ---------------- Database Setup ----------------
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    address TEXT
)
""")
conn.commit()

# ---------------- Functions ----------------
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("⚠ Input Error", "Name and Phone are required")
        return

    cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
                   (name, phone, email, address))
    conn.commit()
    messagebox.showinfo("✅ Success", "Contact added successfully")
    clear_entries()
    view_contacts()

def view_contacts():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM contacts")
    for row in cursor.fetchall():
        listbox.insert(tk.END, f"{row[0]} | {row[1]} - {row[2]}")

def search_contact():
    query = simpledialog.askstring("🔍 Search", "Enter Name or Phone:")
    if not query:
        return
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?",
                   ('%' + query + '%', '%' + query + '%'))
    results = cursor.fetchall()
    if results:
        for row in results:
            listbox.insert(tk.END, f"{row[0]} | {row[1]} - {row[2]}")
    else:
        messagebox.showinfo("Not Found", "No contact found")

def delete_contact():
    selected = listbox.get(tk.ACTIVE)
    if not selected:
        messagebox.showwarning("⚠ Selection Error", "Select a contact to delete")
        return
    contact_id = selected.split(" | ")[0]
    cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    messagebox.showinfo("🗑 Deleted", "Contact deleted successfully")
    view_contacts()

def update_contact():
    selected = listbox.get(tk.ACTIVE)
    if not selected:
        messagebox.showwarning("⚠ Selection Error", "Select a contact to update")
        return

    contact_id = selected.split(" | ")[0]
    cursor.execute("SELECT * FROM contacts WHERE id=?", (contact_id,))
    contact = cursor.fetchone()

    new_name = simpledialog.askstring("✏ Update", "Name:", initialvalue=contact[1]) or contact[1]
    new_phone = simpledialog.askstring("✏ Update", "Phone:", initialvalue=contact[2]) or contact[2]
    new_email = simpledialog.askstring("✏ Update", "Email:", initialvalue=contact[3]) or contact[3]
    new_address = simpledialog.askstring("✏ Update", "Address:", initialvalue=contact[4]) or contact[4]

    cursor.execute("UPDATE contacts SET name=?, phone=?, email=?, address=? WHERE id=?",
                   (new_name, new_phone, new_email, new_address, contact_id))
    conn.commit()
    messagebox.showinfo("✅ Updated", "Contact updated successfully")
    view_contacts()

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# ---------------- UI Setup ----------------
root = tk.Tk()
root.title("📒 Contact Book")
root.geometry("600x500")
root.configure(bg="#f0f4f7")

# --- Title ---
title_label = tk.Label(root, text="📒 Contact Book", font=("Arial", 20, "bold"), bg="#2c3e50", fg="white", pady=10)
title_label.pack(fill="x")

# --- Input Frame ---
input_frame = tk.Frame(root, bg="#f0f4f7", padx=10, pady=10)
input_frame.pack(pady=5, fill="x")

tk.Label(input_frame, text="Name:", bg="#f0f4f7").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(input_frame, width=40)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(input_frame, text="Phone:", bg="#f0f4f7").grid(row=1, column=0, sticky="w")
phone_entry = tk.Entry(input_frame, width=40)
phone_entry.grid(row=1, column=1, pady=5)

tk.Label(input_frame, text="Email:", bg="#f0f4f7").grid(row=2, column=0, sticky="w")
email_entry = tk.Entry(input_frame, width=40)
email_entry.grid(row=2, column=1, pady=5)

tk.Label(input_frame, text="Address:", bg="#f0f4f7").grid(row=3, column=0, sticky="w")
address_entry = tk.Entry(input_frame, width=40)
address_entry.grid(row=3, column=1, pady=5)

add_btn = tk.Button(root, text="➕ Add Contact", command=add_contact, bg="#27ae60", fg="white", font=("Arial", 10, "bold"), width=20)
add_btn.pack(pady=5)

# --- List Frame ---
list_frame = tk.Frame(root, bg="#f0f4f7")
list_frame.pack(pady=10, fill="both", expand=True)

listbox = tk.Listbox(list_frame, width=70, height=12, font=("Courier New", 10))
listbox.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# --- Buttons ---
btn_frame = tk.Frame(root, bg="#f0f4f7")
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="📋 View Contacts", command=view_contacts, bg="#2980b9", fg="white", width=15).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="🔍 Search", command=search_contact, bg="#8e44ad", fg="white", width=15).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="✏ Update", command=update_contact, bg="#f39c12", fg="white", width=15).grid(row=0, column=2, padx=5, pady=5)
tk.Button(btn_frame, text="🗑 Delete", command=delete_contact, bg="#c0392b", fg="white", width=15).grid(row=0, column=3, padx=5, pady=5)

# Load contacts initially
view_contacts()

root.mainloop()
