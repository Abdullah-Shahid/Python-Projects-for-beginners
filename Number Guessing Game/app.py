import random

def number():
    return random.randint(1,100)

def main():
    attempts = 0
    r_number = number()
    print("=== Number Guessing Game 🤔 (1-100) ===")
    while True:
        guess = int(input("Guess the number: "))
        attempts += 1

        if guess > 100:
            print("❌ Invalid guess. Guess the number between 1 and 100.")

        elif guess > r_number:
            print("🔺 Too high, lower number please.")

        elif guess < r_number:
            print("🔻 Too low, higher number please.")

        else:
            print(f"✨ Congratulations, you've guessed the number in {attempts} attempts.")
            break


if __name__ == '__main__':
    main()