import random

# Function to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to display the choices and result
def display_result(user_choice, computer_choice, result):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)

# Main function
def main():
    user_score = 0
    computer_score = 0
    print("Welcome to Rock-Paper-Scissors Game!")

    while True:
        print("\nChoose your move: rock, paper, or scissors")
        user_choice = input("Your choice: ").lower()
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"\nYour score: {user_score}")
        print(f"Computer's score: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
