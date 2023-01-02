import tkinter as tk
import mysql.connector
from tkinter import messagebox


DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "password"
DB_NAME = "login_database"

def check(username, password):
   
    conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_USER, database=DB_NAME)
    cursor = conn.cursor()

    
    cursor.execute("SELECT username, password FROM users WHERE username=%s", (username,))
    result = cursor.fetchone()

    
    if result is None:
        messagebox.showerror("Login Error", "Invalid username or password")
    else:
        stored_username, stored_password = result

        
        if password == stored_password:
            messagebox.showinfo("Login", "Login successful")
        else:
            messagebox.showerror("Login")