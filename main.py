import tkinter as tk
from tkinter import messagebox

def check(username, password):
    
    with open("credentials.txt", "r") as f:
        stored_username = f.readline().strip()
        stored_password = f.readline().strip()
    
    
    if username == stored_username and password == stored_password:
        messagebox.showinfo("Login", "Login successful")
    else:
        messagebox.showerror("Login Error", "Invalid username or password")


window = tk.Tk()
window.geometry("250x250")
window.title("Login form")


tk.Label(window, text="Username:").grid(row=1, column=0)
username_entry = tk.Entry(window)
username_entry.grid(row=1, column=1)

tk.Label(window, text="Password:").grid(row=2, column=0)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=2, column=1)


login_button = tk.Button(window, text="Login", command=lambda: check(username_entry.get(), password_entry.get()))
login_button.grid(row=4, column=1)

window.mainloop()