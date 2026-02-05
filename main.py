import random
"""
Guess The Number Game - Complete Documentation
MODULE: main.py
DESCRIPTION:
    An interactive number guessing game where players try to guess a randomly 
    generated number within a user-defined range. The game provides feedback 
    and hints, tracks scores across multiple rounds, and allows players to 
    compete for the highest total score.
FUNCTIONS:
1. print_banner()
   PURPOSE:
       Displays the welcome banner at the start of the game.
   PARAMETERS:
       None
   RETURN VALUE:
       None
   WORKING:
       Prints a decorative banner with the game title using ASCII art and 
       emoji to create an engaging welcome message.
2. get_range()
   PURPOSE:
       Prompts the user to set the range for the number to be guessed.
   PARAMETERS:
       None
   RETURN VALUE:
       tuple: (start, end) - Two integers representing the range boundaries
   WORKING:
       - Runs in a loop until valid input is received
       - Asks user to input start and end integers
       - Validates that start < end
       - Handles ValueError exceptions for non-integer inputs
       - Returns the valid range tuple
3. generate_random_number(start, end)
   PURPOSE:
       Generates a random number within the specified range.
   PARAMETERS:
       start (int): Lower bound of the range (inclusive)
       end (int): Upper bound of the range (inclusive)
   RETURN VALUE:
       int: A random integer between start and end
   WORKING:
       Uses random.randint() to generate and return a random number 
       within the provided range.
4. get_user_guess()
   PURPOSE:
       Prompts the user to enter their guess.
   PARAMETERS:
       None
   RETURN VALUE:
       int: The user's guessed number
   WORKING:
       - Runs in a loop until valid input is received
       - Converts user input to integer
       - Handles ValueError exceptions for non-integer inputs
       - Returns the validated guess
5. calculate_distance(guess, target)
   PURPOSE:
       Calculates the absolute distance between the guess and target number.
   PARAMETERS:
       guess (int): The number guessed by the player
       target (int): The actual random number to guess
   RETURN VALUE:
       int: Absolute difference between guess and target
   WORKING:
       Uses abs() function to return the absolute difference, which helps 
       determine how close the guess is to the target.
6. show_feedback(guess, target)
   PURPOSE:
       Provides feedback and hints based on the user's guess.
   PARAMETERS:
       guess (int): The number guessed by the player
       target (int): The actual random number
   RETURN VALUE:
       None
   WORKING:
       - Calculates distance between guess and target
       - If distance is 0: announces perfect guess
       - If distance <= 5: shows "Very close" with hint
       - If distance <= 15: shows "Close" with hint
       - If distance > 15: shows "Far off" with hint
       - Hint indicates if target is higher or lower than guess
7. retry_prompt()
   PURPOSE:
       Asks the user if they want to play another round.
   PARAMETERS:
       None
   RETURN VALUE:
       bool: True if user wants to play again, False otherwise
   WORKING:
       - Loops until valid input is received
       - Accepts 'yes', 'y', 'no', 'n' (case-insensitive)
       - Returns True for yes, False for no
       - Displays error for invalid input
8. show_instructions()
   PURPOSE:
       Displays the game rules and instructions to the player.
   PARAMETERS:
       None
   RETURN VALUE:
       None
   WORKING:
       Prints a formatted list of 6 instructions explaining:
       - How to set the range
       - How random number generation works
       - The guessing process
       - Feedback mechanism
       - Scoring system
       - Multi-round gameplay
9. show_summary(round_number, attempts, round_score, total_score)
   PURPOSE:
       Displays the summary of the completed round.
   PARAMETERS:
       round_number (int): Current round number
       attempts (int): Number of guesses made in this round
       round_score (int): Points earned in this round
       total_score (int): Cumulative score across all rounds
   RETURN VALUE:
       None
   WORKING:
       Prints a formatted summary box showing:
       - Current round number
       - Attempts made in the round
       - Score earned in the round
       - Total accumulated score
10. play_game()
    PURPOSE:
        Main game loop that orchestrates the entire game flow.
    PARAMETERS:
        None
    RETURN VALUE:
        None
    WORKING:
        - Shows instructions at start
        - Initializes round counter and total score
        - Main loop:
          * Gets range from user
          * Generates target number
          * Inner loop for guessing:
            - Increments attempt counter
            - Gets player guess
            - Provides feedback
            - Decreases score for each wrong guess
            - Breaks when guess is correct
          * Shows round summary
          * Asks if player wants to continue
          * Continues to next round or exits
        - Displays final score when game ends
11. main()
    PURPOSE:
        Entry point of the program.
    PARAMETERS:
        None
    RETURN VALUE:
        None
    WORKING:
        - Calls print_banner() to display welcome message
        - Calls play_game() to start the game loop
SCORING SYSTEM:
    - Maximum score per round = (end - start + 1)
    - Decreases by 1 for each wrong guess
    - Minimum score per round = 0
    - Total score accumulates across all rounds
GAME FLOW:
    1. Display banner
    2. Show instructions
    3. Get range from user
    4. Generate random number
    5. Loop: Get guess → Provide feedback → Check if correct
    6. Show round summary
    7. Ask to play again
    8. Repeat steps 3-7 or exit with final score
DEPENDENCIES:
    - random: For random.randint() function
    - time: For time.sleep() delays between rounds
"""
import time

def print_banner():
    print("="*70)
    print("        🎲 Welcome to the Ultimate Number Guessing Game! 🎲")
    print("="*70)
    print()

def get_range():
    while True:
        try:
            print("\n🔹 Set your guessing range:")
            start = int(input("Enter the start of the range (integer): "))
            end = int(input("Enter the end of the range (integer): "))
            if start >= end:
                print("Invalid range. Start should be less than end.")
            else:
                return start, end
        except ValueError:
            print("Invalid input. Please enter integers only.")

def generate_random_number(start, end):
    return random.randint(start, end)

def get_user_guess():
    while True:
        try:
            return int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def calculate_distance(guess, target):
    return abs(guess - target)

def show_feedback(guess, target):
    distance = calculate_distance(guess, target)
    if distance == 0:
        print(" Perfect! You've guessed the number!")
    else:
        hint = " Higher!" if guess < target else " Lower!"
        if distance <= 5:
            print(f"Very close! \nHint: {hint}")
        elif distance <= 15:
            print(f"Close! \nHint: {hint}")
        else:
            print(f"Far off! \nHint: {hint}")

def retry_prompt():
    while True:
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def show_instructions():
    print("\nInstructions:")
    print("────────────────────────────────────────────")
    print("1. Set a range by providing a start and end integer.")
    print("2. A random number will be generated within that range.")
    print("3. Try to guess the number.")
    print("4. You will receive feedback and hints after each guess.")
    print("5.  Points are based on how few guesses you take.")
    print("6.  You can play multiple rounds and accumulate your total score!")
    print("────────────────────────────────────────────\n")

def show_summary(round_number, attempts, round_score, total_score):
    print("\n" + "═"*50)
    print(f"Round {round_number} Summary ")
    print("─"*50)
    print(f"Attempts this round: {attempts}")
    print(f"Score this round: {round_score}")
    print(f"Total score: {total_score}")
    print("═"*50 + "\n")

def play_game():
    show_instructions()
    round_number = 1
    total_score = 0

    while True:
        start, end = get_range()
        target_number = generate_random_number(start, end)
        print(f"\n🔢 A random number has been generated between {start} and {end}. Try to guess it!")

        attempts = 0
        max_score = end - start + 1
        round_score = max_score

        while True:
            attempts += 1
            guess = get_user_guess()
            show_feedback(guess, target_number)
            if guess != target_number:
                round_score = max(round_score - 1, 0)
            else:
                time.sleep(0.5)
                break

        total_score += round_score
        show_summary(round_number, attempts, round_score, total_score)

        if retry_prompt():
            round_number += 1
            print("\n✨ Starting next round! ✨\n")
            time.sleep(1)
        else:
            print(f"\n🎯 Game Over! Your final total score: {total_score} 🎯")
            print("Thanks for playing the Ultimate Number Guessing Game!")
            break

def main():
    print_banner()
    play_game()

if __name__ == "__main__":
    main()
