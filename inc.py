

import tkinter as tk
from tkinter import messagebox

def encrypt():
    """Encrypt the input text using the password."""
    plaintext = e1.get()
    password = e5.get()
    ciphertext = ""
    password_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(password[password_index % len(password)]) - ord('a')
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            password_index += 1
        else:
            ciphertext += char
    e2.delete(0, tk.END)
    e2.insert(0, ciphertext)

def decrypt():
    """Decrypt the input ciphertext using the password."""
    ciphertext = e3.get()
    password = e5.get()
    plaintext = ""
    password_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(password[password_index % len(password)]) - ord('a')
            if char.isupper():
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            password_index += 1
        else:
            plaintext += char
    e4.delete(0, tk.END)
    e4.insert(0, plaintext)

# Main window
root = tk.Tk()
root.title("Encryption/Decryption")

# Menu bar
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

# Labels
tk.Label(root, text="Enter text to encrypt:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Encrypted text:").grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, text="Enter encrypted text to decrypt:").grid(row=2, column=0, padx=10, pady=10)
tk.Label(root, text="Decrypted text:").grid(row=3, column=0, padx=10, pady=10)
tk.Label(root, text="Enter password:").grid(row=4, column=0, padx=10, pady=10)

# Entry fields
e1 = tk.Entry(root, width=50)
e1.grid(row=0, column=1, padx=10, pady=10)
e2 = tk.Entry(root, width=50)
e2.grid(row=1, column=1, padx=10, pady=10)
e3 = tk.Entry(root, width=50)
e3.grid(row=2, column=1, padx=10, pady=10)
e4 = tk.Entry(root, width=50)
e4.grid(row=3, column=1, padx=10, pady=10)
e5 = tk.Entry(root, width=50, show="*")  # Show * instead of the actual password characters
e5.grid(row=4, column=1, padx=10, pady=10)

# Buttons
tk.Button(root, text="Encrypt", command=encrypt).grid(row=0, column=2, padx=10, pady=10)
tk.Button(root, text="Decrypt", command=decrypt).grid(row=2, column=2, padx=10, pady=10)

root.mainloop()
