# 🕹️ Arcade Day Pass Tracker — Challenge Steps
#
# 1) Create variables to store:
#    - customer name
#    - number of passes
#    - tokens per pass
#    - price per pass
#    - tokens required per game
#
# 2) Calculate:
#    - total tokens
#    - total cost
#    - games available  (use 'floor division' to get a whole number)
#
# 3) Print a summary with:
#    - customer name
#    - passes bought
#    - total tokens
#    - total cost

import tkinter as tk
from tkinter import ttk


name = " Allice Jan Dark de la Cruz"
num_passes = 3
tokens_per_pass = 50
price_per_pass = 20.0
tokens_per_game = 5

total_tokens = num_passes * tokens_per_pass
total_cost = num_passes * price_per_pass
games_available = total_tokens // tokens_per_game
print("Customer Name:", name)
print("Passes Bought:", num_passes) 
print("Total Tokens:", total_tokens)
print("Total Cost: $", total_cost)
print("Games Available:", games_available)
# 🧮 Simple Calculator with Tkinter — Challenge Steps

#Create a GUI with Tkinter

#Create the main window
window = tk.Tk()
window.title("🕹️ Arcade Day Pass Tracker")
window.geometry("300x200")

# Configure grid column to expand (so centering works)
window.grid_columnconfigure(0, weight=1)

# Labels centered in column 0
tk.Label(window, text = "Name: " + name).grid(row=0, column=0,sticky="nsew")
tk.Label(window, text = "Pass number :"  + str(num_passes)).grid(row=1, column=0, sticky="nsew")
tk.Label(window, text = "Total Tokens: " + str(total_tokens)).grid(row=2, column=0, sticky="nsew")
tk.Label(window, text = "Total Cost: $" + str(total_cost)).grid(row=3, column=0, sticky="nsew")
tk.Label(window, text = "Games Available: " + str(games_available)).grid(row=4, column=0, sticky="nsew")

window.mainloop()