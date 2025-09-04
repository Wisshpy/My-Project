import tkinter as tk

# Functions for calculator operations

def add():
    try:
        result.set(float(entry1.get()) + float(entry2.get()))
    except ValueError:
        result.set("Error")

def subtract():
    try:
        result.set(float(entry1.get()) - float(entry2.get()))
    except ValueError:
        result.set("Error")

def multiply():
    try:
        result.set(float(entry1.get()) * float(entry2.get()))
    except ValueError:
        result.set("Error")

def divide():
    try:
        if float(entry2.get()) == 0:
            result.set("Cannot divide by zero")
        else:
            result.set(float(entry1.get()) / float(entry2.get()))   
    except ValueError:
        result.set("Error")

# Setting up the main window
window = tk.Tk()
window.title("Simple Calculator")

# Input fields
tk.Label(window, text = "Enter first number:").grid(row=0, column=0)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)

tk.Label(window, text = "Enter second number:").grid(row=1, column=0)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)

# Result display
result = tk.StringVar()
tk.Label(window, text = "Result:").grid(row=2, column=0)
tk.Label(window, textvariable=result).grid(row=2, column=1)

# Operation buttons
tk.Button(window, text="+", command=add).grid(row=3, column=0)
tk.Button(window, text="-", command=subtract).grid(row=3, column=1)
tk.Button(window, text="*", command=multiply).grid(row=4, column=0)
tk.Button(window, text="/", command=divide).grid(row=4, column=1)

# Run the application
window.mainloop()
