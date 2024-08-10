import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")

        # Password length
        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_var = tk.IntVar(value=8)
        self.length_entry = tk.Entry(master, textvariable=self.length_var, width=5)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        # Character options
        self.letters_var = tk.BooleanVar(value=True)
        self.letters_check = tk.Checkbutton(master, text="Include Letters", variable=self.letters_var)
        self.letters_check.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.numbers_var = tk.BooleanVar(value=True)
        self.numbers_check = tk.Checkbutton(master, text="Include Numbers", variable=self.numbers_var)
        self.numbers_check.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.symbols_var = tk.BooleanVar(value=True)
        self.symbols_check = tk.Checkbutton(master, text="Include Symbols", variable=self.symbols_var)
        self.symbols_check.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        # Generate button
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Password display
        self.password_display = tk.Entry(master, width=30, state='readonly')
        self.password_display.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Copy to clipboard button
        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        length = self.length_var.get()
        use_letters = self.letters_var.get()
        use_numbers = self.numbers_var.get()
        use_symbols = self.symbols_var.get()

        char_pool = ''
        if use_letters:
            char_pool += string.ascii_letters
        if use_numbers:
            char_pool += string.digits
        if use_symbols:
            char_pool += string.punctuation

        if not char_pool:
            messagebox.showerror("Error", "At least one character type must be selected")
            return

        password = ''.join(random.choice(char_pool) for _ in range(length))
        self.password_display.config(state='normal')
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)
        self.password_display.config(state='readonly')

    def copy_to_clipboard(self):
        password = self.password_display.get()
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
