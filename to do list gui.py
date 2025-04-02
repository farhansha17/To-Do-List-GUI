import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def mark_done():
    try:
        selected_task = listbox.curselection()[0]
        task = listbox.get(selected_task)
        listbox.delete(selected_task)
        listbox.insert(tk.END, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as done!")

# GUI Setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

tk.Label(root, text="Enter a Task:").pack()
entry = tk.Entry(root, width=40)
entry.pack()

tk.Button(root, text="Add Task", command=add_task).pack()
tk.Button(root, text="Mark as Done", command=mark_done).pack()
tk.Button(root, text="Delete Task", command=delete_task).pack()

listbox = tk.Listbox(root, width=50, height=15)
listbox.pack()

root.mainloop()