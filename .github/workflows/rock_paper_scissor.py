import os
import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from playsound import playsound


class Game:
    def __init__(self):
        # options available to plays
        self.options = ["rock", "paper", "scissors"]
        # winning combinations of the game
        self.winning_combinations = {("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")}
        # number of times the user wins
        self.user_wins = 0
        # number of times the computer wins
        self.computer_wins = 0
        # number of times the game ends in a draw
        self.draws = 0
        # sounds to play when the user wins, loses, or draws
        self.win_sound = os.path.join("sounds", "win.wav")
        self.lose_sound = os.path.join("sounds", "lose.wav")
        self.draw_sound = os.path.join("sounds", "draw.wav")

    def play(self, user_input):
        # check if user wants to quit
        if user_input == "q":
            return False

        # check for invalid input
        if user_input not in self.options:
            return True

        # computer selects a random option
        computer_pick = random.choice(self.options)

        # check if user wins, loses, or draws
        if (user_input, computer_pick) in self.winning_combinations:
            self.user_wins += 1
            result_label.config(text="You won!", foreground="green")
            # play win sound
            playsound(self.win_sound)
        elif user_input == computer_pick:
            self.draws += 1
            result_label.config(text="It's a Draw!", foreground="orange")
            # play draw sound
            playsound(self.draw_sound)
        else:
            self.computer_wins += 1
            result_label.config(text="You lost!", foreground="red")
            # play lose sound
            playsound(self.lose_sound)

        # update score label
        score_label.config(text=f"Score: {self.user_wins} - {self.computer_wins} - {self.draws}")
        return True

    def reset_game(self):
        # reset game statistics
        self.user_wins = 0
        self.computer_wins = 0
        self.draws = 0

        # update GUI labels
        score_label.config(text="Score: 0 - 0 - 0")
        result_label.config(text="", foreground="black")

    def quit(self):
        window.destroy()


# create a new game instance
game = Game()

# create the GUI window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("800x500")

# load images
rock_img = ImageTk.PhotoImage(Image.open("images/rock.png").resize((150, 150)))
paper_img = ImageTk.PhotoImage(Image.open("images/paper.png").resize((150, 150)))
scissors_img = ImageTk.PhotoImage(Image.open("images/scissors.png").resize((150, 150)))
reset_img = ImageTk.PhotoImage(Image.open("images/reset.png").resize((40, 40)))
quit_img = ImageTk.PhotoImage(Image.open("images/quit.png").resize((40, 40)))


# create the widgets
title_label = tk.Label(
    window,
    text="Rock Paper Scissors",
    font=("Helvetica", 32, "bold"),
    bg="#383838",
    fg="white",
    padx=20,
    pady=20,
)
instruction_label = tk.Label(
    window,
    text="Select an option below to play against the computer:",
    font=("Helvetica", 14),
    bg="#383838",
    fg="white",
)
button_frame = tk.Frame(window, bg="#383838")
rock_button = tk.Button(
    button_frame,
    image=rock_img,
    command=lambda: game.play("rock"),
    bd=0,
    highlightthickness=0,
)
paper_button = tk.Button(
    button_frame,
    image=paper_img,
    command=lambda: game.play("paper"),
    bd=0,
    highlightthickness=0,
)
scissors_button = tk.Button(
    button_frame,
    image=scissors_img,
    command=lambda: game.play("scissors"),
    bd=0,
    highlightthickness=0,
)
result_label = tk.Label(
    window,
    text="",
    font=("Helvetica", 24, "bold"),
    bg="#383838",
    fg="white",
    pady=20,
)
score_label = tk.Label(
    window,
    text="Score: 0 - 0 - 0",
    font=("Helvetica", 14),
    bg="#383838",
    fg="white",
    pady=10,
)
reset_button = tk.Button(
    window,
    image=reset_img,
    command=game.reset_game,
    bd=0,
    highlightthickness=0,
    bg="#383838",
    activebackground="#383838",
)
quit_button = tk.Button(
    window,
    image=quit_img,
    command=game.quit,
    bd=0,
    highlightthickness=0,
    bg="#383838",
    activebackground="#383838",
)

# arrange the widgets in the window
title_label.pack(pady=20)
instruction_label.pack()
button_frame.pack(pady=20)
rock_button.grid(row=0, column=0, padx=10)
paper_button.grid(row=0, column=1, padx=10)
scissors_button.grid(row=0, column=2, padx=10)
result_label.pack(pady=20)
score_label.pack()
reset_button.pack(side="left", padx=20)
quit_button.pack(side="right", padx=20, pady=10)

# run the GUI
window.mainloop()
