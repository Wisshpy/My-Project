import tkinter as tk
from tkinter import messagebox  

#Trivia questions and answers
questions = [ 
    { 
        "question": "What is the capital of France?", 
        "options": ["Berlin", "Madrid", "Paris", "Rome"], 
        "answer": "Paris" 
    }, 
    { 
        "question": "Which planet is known as the Red Planet?", 
        "options": ["Earth", "Mars", "Jupiter", "Saturn"], 
        "answer": "Mars" 
    }, 
    { 
        "question": "Who wrote 'To Kill a Mockingbird'?", 
        "options": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"], 
        "answer": "Harper Lee" 
    }
]

#Game State

curent_question = 0 
score = 0

#Function

def load_question():
    global curent_question
    q = questions[curent_question]
    question_label.config(text=q["question"])
    for i, option_text in enumerate(q["options"]):
        option_buttons[i].config(text=option_text)

def check_answer(answer):
    global curent_question, score
    q = questions[curent_question]
    if answer == q["answer"]:
        score += 1
    curent_question += 1
    if curent_question < len(questions):
        load_question()
    else:
        messagebox.showinfo("Game Over", f"Your score is {score}/{len(questions)}")
        root.destroy()

#UI Setup
root = tk.Tk()
root.title("Trivia Game")

question_label = tk.Label(root, 
    text="",
     font=("Arial", 16),
       wraplength = 400,
         justify="center")
   
question_label.pack(pady=20)

option_buttons = []
for i in range(4):
    btn = tk.Button(
        root,
        text="",
        font=("Arial", 12),
        width=30,
        command=lambda i=i: check_answer(option_buttons[i].cget("text"))
    )
    btn.pack(pady=5)
    option_buttons.append(btn)

#Start the game
load_question()
root.mainloop()
