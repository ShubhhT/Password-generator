import tkinter as tk
from tkinter import messagebox, ttk
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Password Generator")
        self.root.geometry("450x350")
        self.root.configure(bg="#3776ab")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Password Length:", bg="#3776ab").pack(pady=5)
        
        self.length_var = tk.IntVar()
        self.length_entry = tk.Entry(self.root, textvariable=self.length_var, width=5)
        self.length_entry.pack(pady=5)
        
        self.include_uppercase = tk.BooleanVar()
        tk.Checkbutton(self.root, text="Include Uppercase", variable=self.include_uppercase, bg="#3776ab").pack(pady=5)
        
        self.include_numbers = tk.BooleanVar()
        tk.Checkbutton(self.root, text="Include Numbers", variable=self.include_numbers, bg="#3776ab").pack(pady=5)
        
        self.include_symbols = tk.BooleanVar()
        tk.Checkbutton(self.root, text="Include Symbols", variable=self.include_symbols, bg="#3776ab").pack(pady=5)
        
        self.password_var = tk.StringVar()
        password_entry = tk.Entry(self.root, textvariable=self.password_var, state='readonly', width=35)
        password_entry.pack(pady=5)
        
        self.strength_var = tk.StringVar()
        strength_label = tk.Label(self.root, textvariable=self.strength_var, bg="#f0f0f0")
        strength_label.pack(pady=5)

        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=5)
        
        generate_btn = tk.Button(self.root, text="Generate Password", command=self.generate_password, bg="#4caf50", fg="white")
        generate_btn.pack(pady=5)
        copy_btn = tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard, bg="#2196f3", fg="white")
        copy_btn.pack(pady=5)

    def generate_password(self):
        length = self.length_var.get()
        
        if length <= 0:
            messagebox.showerror("Error", "Please enter a valid length")
            return

        char_set = string.ascii_lowercase
        if self.include_uppercase.get():
            char_set += string.ascii_uppercase
        if self.include_numbers.get():
            char_set += string.digits
        if self.include_symbols.get():
            char_set += string.punctuation
        
        password = ''.join(random.choice(char_set) for _ in range(length))
        self.password_var.set(password)
        self.progress["value"] = length * 10 if length <= 20 else 300
        self.root.update_idletasks()
        self.update_strength_indicator(password)

    def update_strength_indicator(self, password):
        if len(password) < 5:
            self.strength_var.set("Weak Password")
        elif len(password) < 9:
            self.strength_var.set("Moderate Password")
        else:
            self.strength_var.set("Strong Password")
        
    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard")
        else:
            messagebox.showerror("Error", "No password generated")

def start_app():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
    
if __name__ == "__main__":
    start_app()
