
def main():
    # Initialize modules
    score_manager = Score()
    user_manager = UserManager()
    dice_game = DiceGame()

    # Load existing scores
    score_manager.load_scores()

    while True:
        # Main menu
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            # Registration
            username = input("Enter username: ")
            password = input("Enter password: ")
            if user_manager.register_user(username, password):
                print("Registration successful.")
        elif choice == '2':
            # Login
            username = input("Enter username: ")
            password = input("Enter password: ")
            if user_manager.login(username, password):
                # Logged in successfully
                while True:
                    print("1. Start Game")
                    print("2. View Top Scores")
                    print("3. Logout")
                    inner_choice = input("Enter choice: ")

                    if inner_choice == '1':
                        # Start game
                        dice_game.play_game()
                        # Update scores
                        score_manager.update_scores(user_manager.users[username], dice_game.stage_wins['user'] * 3)
                        score_manager.save_scores()
                    elif inner_choice == '2':
                        # View top scores
                        top_scores = score_manager.get_top_scores()
                        print("Top Scores:")
                        for username, score in top_scores:
                            print(f"{username}: {score}")
                    elif inner_choice == '3':
                        # Logout
                        user_manager.logout()
                        break
                    else:
                        print("Invalid choice")
        elif choice == '3':
            # Exit
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()