import random

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

    def play(self):
        # prompt user for input and convert to lower case
        user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
        
        # check if user wants to quit
        if user_input == "q":
            print(self.show_final_score())
            return False
        
        # check for invalid input
        if user_input not in self.options:
            print("Invalid input, please try again.")
            return True
        
        # computer selects a random option
        computer_pick = random.choice(self.options)
        
        # check if user wins, loses, or draws
        if (user_input, computer_pick) in self.winning_combinations:
            self.user_wins += 1
            print("You won!")
        elif user_input == computer_pick:
            self.draws += 1
            print("It's a Draw!")
        else:
            self.computer_wins += 1
            print("You lost!")
        return True
    
    #Show the final score of the game
    def show_final_score(self):
        return f"You won {self.user_wins} times. The computer won {self.computer_wins} times. Draws {self.draws} times. Goodbye!"
# create a new game instance
game = Game()

# play the game in a loop until user quits
while game.play():
    continue

# print the final score
print(game.show_final_score())
