import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

def fetch_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_task():
    title = entry_title.get()
    description = entry_description.get()
    deadline = entry_deadline.get()
    priority = priority_var.get()

    if not title or not deadline:
        messagebox.showwarning("Input Error", "Judul dan Deadline harus diisi!")
        return

    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO tasks (title, description, deadline, priority) VALUES (?, ?, ?, ?)
    ''', (title, description, deadline, priority))
    conn.commit()
    conn.close()
    refresh_table()
    clear_form()

def clear_form():
    entry_title.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    entry_deadline.delete(0, tk.END)
    priority_var.set("Rendah")

def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    for task in fetch_tasks():
        tree.insert('', tk.END, values=task)

# Setup GUI
root = tk.Tk()
root.title("Pengelola Tugas Harian")

frame_form = tk.Frame(root)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Judul").grid(row=0, column=0, padx=5, pady=5)
entry_title = tk.Entry(frame_form)
entry_title.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Deskripsi").grid(row=1, column=0, padx=5, pady=5)
entry_description = tk.Entry(frame_form)
entry_description.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Deadline").grid(row=2, column=0, padx=5, pady=5)
entry_deadline = tk.Entry(frame_form)
entry_deadline.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Prioritas").grid(row=3, column=0, padx=5, pady=5)
priority_var = tk.StringVar(value="Rendah")
priority_menu = ttk.Combobox(frame_form, textvariable=priority_var, values=["Rendah", "Sedang", "Tinggi"])
priority_menu.grid(row=3, column=1, padx=5, pady=5)

btn_add = tk.Button(frame_form, text="Tambah Tugas", command=add_task)
btn_add.grid(row=4, columnspan=2, pady=10)

# Tabel Tugas
columns = ("ID", "Judul", "Deskripsi", "Deadline", "Prioritas", "Status")
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
tree.pack(fill=tk.BOTH, expand=True)

refresh_table()
root.mainloop()
