import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    return random.choice(['stone', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'stone') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!", 1
    else:
        return "Computer wins!", -1

class Game:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

    def play_game(self, user_choice):
        computer_choice = get_computer_choice()
        result, score = determine_winner(user_choice, computer_choice)
        self.user_score += score
        self.computer_score -= score
        message = f"Your choice: {user_choice} {get_symbol(user_choice)}\nComputer's choice: {computer_choice} {get_symbol(computer_choice)}\n\n"
        message += f"{result}\n\nYour Score: {self.user_score}\nComputer's Score: {self.computer_score}"
        messagebox.showinfo("Result", message)

def get_symbol(choice):
    if choice == 'stone':
        return "\u270A"  # Fist symbol
    elif choice == 'paper':
        return "\u270B"  # Raised hand symbol
    else:
        return "\u270C"  # Victory hand symbol

def main():
    root = tk.Tk()
    root.title("Stone-Paper-Scissors")

    game = Game()

    def on_button_click(choice):
        game.play_game(choice)
        update_scores()

    choices = ['stone', 'paper', 'scissors']
    for choice in choices:
        button = tk.Button(root, text=get_symbol(choice), font=('Arial', 20), command=lambda c=choice: on_button_click(c))
        button.pack(side=tk.LEFT, padx=10, pady=10)

    score_label = tk.Label(root, text="Scores", font=('Arial', 16, 'bold'))
    score_label.pack(pady=20)

    score_frame = tk.Frame(root)
    score_frame.pack()

    user_score_label = tk.Label(score_frame, text="Your Score:", font=('Arial', 12))
    user_score_label.grid(row=0, column=0, padx=5)

    user_score_value = tk.Label(score_frame, text="0", font=('Arial', 12, 'bold'), fg='green')
    user_score_value.grid(row=0, column=1, padx=5)

    computer_score_label = tk.Label(score_frame, text="Computer's Score:", font=('Arial', 12))
    computer_score_label.grid(row=1, column=0, padx=5)

    computer_score_value = tk.Label(score_frame, text="0", font=('Arial', 12, 'bold'), fg='red')
    computer_score_value.grid(row=1, column=1, padx=5)

    def update_scores():
        user_score_value.config(text=str(game.user_score))
        computer_score_value.config(text=str(game.computer_score))

    root.mainloop()

if __name__ == "__main__":
    main()
