import secrets
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def generate_password():
    # get length
    try:
        length = int(length_entry.get())
        if not (8 <= length <= 100):
            messagebox.showerror("Error", "Length must be between 8 and 100!")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")
        return

    # building character pool based on checkboxes
    chars = string.ascii_lowercase + string.ascii_uppercase
    if use_digits_var.get():
        chars += string.digits
    if use_symbols_var.get():
        chars += "!@#$%^&*()_-+=[]{};:,.?"

    # generate password
    password = "".join(secrets.choice(chars) for _ in range(length))

    # display result
    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)
    result_entry.config(state="readonly")


def copy_to_clipboard():
    password = result_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")


# main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("600x520")
root.resizable(False, False)

# password length
tk.Label(root, text="Password Length (8-100):", font=("Arial", 10)).pack(pady=(15, 5))
length_entry = tk.Entry(root, font=("Arial", 10), justify="center", width=10)
length_entry.insert(0, "16")
length_entry.pack()

# settings
use_digits_var = tk.BooleanVar(value=True)
use_symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Digits (0-9)", variable=use_digits_var).pack(anchor="w", padx=50, pady=(10, 0))
tk.Checkbutton(root, text="Include Symbols (!@#$...)", variable=use_symbols_var).pack(anchor="w", padx=50)

# generate button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5)
generate_btn.pack(pady=15)

# password display field
result_entry = tk.Entry(root, font=("Consolas", 11), justify="center", width=60, state="readonly")
result_entry.pack(pady=5)

# copy button
copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_btn.pack(pady=5)

root.mainloop()