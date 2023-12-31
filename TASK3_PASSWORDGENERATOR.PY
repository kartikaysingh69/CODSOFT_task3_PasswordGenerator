import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()
    characters = ""

    if include_symbols_var.get():
        characters += string.punctuation
    if include_uppercase_var.get():
        characters += string.ascii_uppercase
    if include_lowercase_var.get():
        characters += string.ascii_lowercase
    if include_digits_var.get():
        characters += string.digits

    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text=password)

window = tk.Tk()
window.title("Password Generator")
window.configure(bg="light grey")

length_label = tk.Label(window, text="Password Length:", bg="light grey")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

complexity_label = tk.Label(window, text="Password Complexity:", bg="light grey")
complexity_label.pack()

complexity_var = tk.IntVar()
complexity_simple = tk.Radiobutton(window, text="Simple", variable=complexity_var, value=1, bg="light grey")
complexity_medium = tk.Radiobutton(window, text="Medium", variable=complexity_var, value=2, bg="light grey")
complexity_complex = tk.Radiobutton(window, text="Complex", variable=complexity_var, value=3, bg="light grey")
complexity_simple.pack()
complexity_medium.pack()
complexity_complex.pack()

include_symbols_var = tk.IntVar()
include_symbols_checkbox = tk.Checkbutton(window, text="Include Symbols", variable=include_symbols_var, bg="light grey")
include_symbols_checkbox.pack()

include_uppercase_var = tk.IntVar()
include_uppercase_checkbox = tk.Checkbutton(window, text="Include Uppercase Letters", variable=include_uppercase_var, bg="light grey")
include_uppercase_checkbox.pack()

include_lowercase_var = tk.IntVar()
include_lowercase_checkbox = tk.Checkbutton(window, text="Include Lowercase Letters", variable=include_lowercase_var, bg="light grey")
include_lowercase_checkbox.pack()

include_digits_var = tk.IntVar()
include_digits_checkbox = tk.Checkbutton(window, text="Include Digits", variable=include_digits_var, bg="light grey")
include_digits_checkbox.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_password, bg="black", fg="white")
generate_button.pack()

password_label = tk.Label(window, text="", font=("Helvetica", 12), bg="light grey")
password_label.pack()

window.mainloop()
