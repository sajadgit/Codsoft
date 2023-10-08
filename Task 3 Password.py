import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()
    
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        result_label.config(text="Please select at least one character type.")
    else:
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text="Generated Password: " + password)

def reset_password():
    result_label.config(text="Generated Password: ")

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry('400x250')  # Increased height for the additional controls

# Set the background color
window.configure(bg="#81d4fa")  # Background color

# Create widgets
length_label = tk.Label(window,bg='#81d4fa', text="Password Length:")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(window,bg='#81d4fa', text="Uppercase Letters", variable=uppercase_var)
uppercase_checkbox.pack()

lowercase_var = tk.BooleanVar()
lowercase_checkbox = tk.Checkbutton(window,bg='#81d4fa', text="Lowercase Letters", variable=lowercase_var)
lowercase_checkbox.pack()

digits_var = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(window,bg='#81d4fa', text="Digits", variable=digits_var)
digits_checkbox.pack()

special_var = tk.BooleanVar()
special_checkbox = tk.Checkbutton(window,bg='#81d4fa', text="Special Characters", variable=special_var)
special_checkbox.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

reset_button = tk.Button(window, text="Reset Password", command=reset_password)
reset_button.pack()

result_label = tk.Label(window,bg='#14A44D', text="Generated Password: ",fg="white")
result_label.pack()

# Customize the appearance
generate_button.configure(bg="#3B71CA", fg="white")  # Background and text color for Generate button
reset_button.configure(bg="#9FA6B2", fg="white")  # Background and text color for Reset button

# Center the window
window.eval('tk::PlaceWindow . center')

# Start the GUI event loop
window.mainloop()






