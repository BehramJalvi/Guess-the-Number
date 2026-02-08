import random
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
    print("─"*50)
    print("1. Set a range by providing a start and end integer.")
    print("2. A random number will be generated within that range.")
    print("3. Try to guess the number.")
    print("4. You will receive feedback and hints after each guess.")
    print("5.  Points are based on how few guesses you take.")
    print("6.  You can play multiple rounds and accumulate your total score!")
    print("─"*50+"\n")

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
