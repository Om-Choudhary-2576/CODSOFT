import random

def play_game():
    user_score = 0
    computer_score = 0
    options = ["rock", "paper", "scissors"]

    print("--- Welcome to Rock-Paper-Scissors ---")

    while True:
        print(f"\nScore -> You: {user_score} | Computer: {computer_score}")
        user_choice = input("Choose rock, paper, or scissors (or 'exit' to quit): ").lower()

        if user_choice == 'exit':
            print("Thanks for playing!")
            break

        if user_choice not in options:
            print("Invalid choice, please try again.")
            continue

       
        computer_choice = random.choice(options)
        

        
        if user_choice == computer_choice:
            print("It's a tie!")
            print(f"Computer chose: {computer_choice}")
        elif ((user_choice == "rock" and computer_choice == "scissors") or
             (user_choice == "scissors" and computer_choice == "paper") or 
             (user_choice == "paper" and computer_choice == "rock")):
            print("You win this round!")
            print(f"Computer chose: {computer_choice}")
            user_score += 1
        else:
            print("You lose this round!")
            print(f"Computer chose: {computer_choice}")
            computer_score += 1

        
        again = input("Play another round? (y/n): ").lower()
        if again != 'y':
            print(f"\nFinal Score - You: {user_score} | Computer: {computer_score}")
            print("Goodbye!")
            break




play_game()