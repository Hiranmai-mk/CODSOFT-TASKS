
import random

def get_user_choice():
    """Get the user's choice."""
    while True:
        choice = input("Enter stone, paper, or scissors: ").lower()
        if choice in ['stone', 'paper', 'scissors']:
            return choice
        print("Invalid choice. Please choose 'stone', 'paper', or 'scissors'.")

def get_computer_choice():
    """Get the computer's choice."""
    return random.choice(['stone', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return 'draw'
    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'stone'):
        return 'user'
    else:
        return 'computer'

def print_result(user_choice, computer_choice, winner):
    """Print the result of the game."""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == 'draw':
        print("It's a draw!")
    elif winner == 'user':
        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    """Play a single round of Stone, Paper, Scissors."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    print_result(user_choice, computer_choice, winner)

def main():
    """Main function to control the game loop."""
    print("Welcome to Stone, Paper, Scissors!")
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
