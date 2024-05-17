import random
import os

def clear_screen():
    # Clear screen based on the operating system
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class DiceGame:
    def __init__(self):
        self.rounds = 3
        self.stage_wins = {'user': 0, 'computer': 0}
        self.user_score = 0
        self.computer_score = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def play_round(self):
        user_roll = self.roll_dice()
        comp_roll = self.roll_dice()
        print(f"User rolled: {user_roll}")
        print(f"Computer rolled: {comp_roll}")
        if user_roll > comp_roll:
            print("User wins this round!")
            return 'user'
        elif user_roll < comp_roll:
            print("Computer wins this round!")
            return 'computer'
        else:
            print("It's a tie!")
            return None

    def play_stage(self):
        self.stage_wins = {'user': 0, 'computer': 0}  # Reset for each stage
        for _ in range(self.rounds):
            winner = self.play_round()
            if winner:
                self.stage_wins[winner] += 1
            input("Press Enter to continue to the next round...")
            clear_screen()
        if self.stage_wins['user'] >= 2:
            self.user_score += 3
            print("Congratulations! You won this stage.")
            return True
        else:
            self.computer_score += 3
            print("Sorry, you lost this stage.")
            return False

    def play_game(self):
        print("Let's play the dice game!")
        stage = 1
        while True:
            print(f"Stage {stage}:")
            if not self.play_stage():
                print("Game over.")
                break
            else:
                print(f"Current Score - User: {self.user_score}, Computer: {self.computer_score}")
                choice = input("Do you want to continue to the next stage? (yes/no): ").lower()
                if choice != 'yes':
                    print("Game ended.")
                    break
                stage += 1
                clear_screen()
        print(f"Final Score : {self.user_score}")
