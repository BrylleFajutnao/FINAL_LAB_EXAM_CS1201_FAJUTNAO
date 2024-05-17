
from utils.score import Score
from utils.usermanager import UserManager
from utils.dice_game import DiceGame
import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    # Initialize modules
    score_manager = Score()
    user_manager = UserManager()
    dice_game = DiceGame()

    # Load existing scores
    score_manager.load_scores()

    while True:
        clear_screen()
        print("Dige Game Login")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            clear_screen()
            username = input("Enter username: ")
            password = input("Enter password: ")
            if user_manager.register_user(username, password):
                print("Registration successful.")
            input("Press Enter to continue...")
        elif choice == '2':
            clear_screen()
            username = input("Enter username: ")
            password = input("Enter password: ")
            if user_manager.login(username, password):
                current_user = user_manager.users[username]
                while True:
                    clear_screen()
                    print("Welcome, "f"{username}")
                    print("1. Start Game")
                    print("2. View Top Scores")
                    print("3. Logout")
                    inner_choice = input("Enter choice: ")

                    if inner_choice == '1':
                        clear_screen()
                        dice_game.play_game()
                        score_manager.update_scores(current_user, dice_game.user_score)
                        score_manager.save_scores()
                        user_manager.save_users() 
                        input("Press Enter to continue...")
                    elif inner_choice == '2':
                        clear_screen()
                        top_scores = score_manager.get_top_scores()
                        print("Top Scores:")
                        for i, (username, score) in enumerate(top_scores, start=1):
                            print(f"{i}. {username}: {score}")
                        input("Press Enter to continue...")
                    elif inner_choice == '3':
                        user_manager.logout()
                        break
                    else:
                        print("Invalid choice")
                        input("Press Enter to continue...")
            else:
                input("Press Enter to continue...")
        elif choice == '3':
            break
        else:
            print("Invalid choice")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
