import random


def play_game():
    secret_number = random.randint(1, 100)

    print("🎮 NUMBER GUESSING GAME")
    print("----------------------")

    print("Choose difficulty:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")

    difficulty_choice = input("\nChoice: ")

    if difficulty_choice == "1":
        max_attempts = 10
    elif difficulty_choice == "2":
        max_attempts = 7
    elif difficulty_choice == "3":
        max_attempts = 5
    else:
        print("Invalid choice, defaulting to Medium (7 attempts).")
        max_attempts = 7

    guess = 0
    attempts = 0

    print("\nI have chosen a number between 1 and 100.")
    print("Try to guess it!\n")

    while guess != secret_number and attempts < max_attempts:

        user_input = input("Guess a number: ")

        try:
            guess = int(user_input)

        except ValueError:
            print("❌ Please enter a valid number!")
            continue

        if guess < 1 or guess > 100:
            print("❌ Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("📉 Too low!")

        elif guess > secret_number:
            print("📈 Too high!")

        else:
            print("\n🎉 Congratulations!")
            print(f"You guessed the number in {attempts} attempts.")
            break

        remaining = max_attempts - attempts

        if remaining > 0:
            print(f"Attempts remaining: {remaining}\n")


    if guess != secret_number:
        print("\n❌ Game Over!")
        print(f"The number was {secret_number}")


play_game()