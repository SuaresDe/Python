import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showwarning("Invalid Input", "The length must be greater than zero.")
            return
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number.")
        return
    
    include_caps = var_caps.get()
    include_lows = var_lows.get()
    include_numbers = var_numbers.get()
    include_specials = var_specials.get()

    if not (include_caps or include_lows or include_numbers or include_specials):
        messagebox.showwarning("Selection Required", "Select at least one character type.")
        return
    
    characters = ""
    password = []

    if include_caps:
        characters += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))

    if include_lows:
        characters += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))

    if include_numbers:
        characters += string.digits
        password.append(random.choice(string.digits))
    
    if include_specials:
        characters += string.punctuation
        password.append(random.choice(string.punctuation))

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    password = "".join(password[:length])

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied!", "Password copied to clipboard.")

main_window = tk.Tk()
main_window.title("Password Generator")
main_window.configure(bg="white")

width_window, height_window = 400, 400
width_screen = main_window.winfo_screenwidth()
height_screen = main_window.winfo_screenheight()
position_x = (width_screen // 2) - (width_window // 2)
position_y = (height_screen // 2) - (height_window // 2)
main_window.geometry(f"{width_window}x{height_window}+{position_x}+{position_y}")

frame_options = tk.LabelFrame(main_window, text="Character Options", padx=10, pady=10, bg="white")
frame_options.pack(pady=20, padx=20, fill="both", expand="yes")

var_caps = tk.BooleanVar()
var_lows = tk.BooleanVar()
var_numbers = tk.BooleanVar()
var_specials = tk.BooleanVar()

check_caps = tk.Checkbutton(frame_options, text="Include Uppercase Letters", variable=var_caps, bg="white")
check_caps.grid(row=0, column=0, sticky="w")

check_lows = tk.Checkbutton(frame_options, text="Include Lowercase Letters", variable=var_lows, bg="white")
check_lows.grid(row=1, column=0, sticky="w")

check_numbers = tk.Checkbutton(frame_options, text="Include Numbers", variable=var_numbers, bg="white")
check_numbers.grid(row=2, column=0, sticky="w")

check_specials = tk.Checkbutton(frame_options, text="Include Special Characters", variable=var_specials, bg="white")
check_specials.grid(row=3, column=0, sticky="w")

length_frame = tk.Frame(main_window, bg="white")
length_frame.pack(pady=10)
length_label = tk.Label(length_frame, text="Number of Characters:", bg="white")
length_label.pack(side="left", padx=5)
length_entry = tk.Entry(length_frame, width=5)
length_entry.pack(side="left", padx=5)

generate_button = tk.Button(main_window, text="Generate Password", command=generate_password, bg="lightgray", width=20)
generate_button.pack(pady=10)

password_frame = tk.Frame(main_window, bg="white")
password_frame.pack(pady=10)

password_label = tk.Label(password_frame, text="Password:", bg="white")
password_label.pack(side="left", padx=5)

password_entry = tk.Entry(password_frame, width=30, font=("Helvetica", 14), state="normal")
password_entry.pack(side="left", padx=5)

copy_button = tk.Button(main_window, text="Copy Password", command=copy_to_clipboard, bg="lightgray", width=20)
copy_button.pack(pady=10)

main_window.mainloop() 