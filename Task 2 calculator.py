import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.title("Calculator")
root.geometry("350x450")  
root.configure(bg="#332d2d")  

screen = tk.StringVar()

entry = tk.Entry(root, textvar=screen, font="lucida 20 bold")
entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

frame = tk.Frame(root, bg="#332d2d")  
frame.pack()

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

row, col = 1, 0

for button in buttons:
    btn = tk.Button(frame, text=button, padx=20, pady=20, font="lucida 15 bold", bg="#E4A11B", fg="white")
    btn.grid(row=row, column=col, padx=5, pady=5)  
    btn.bind("<Button-1>",click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
