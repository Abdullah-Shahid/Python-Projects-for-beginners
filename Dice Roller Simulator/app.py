import random

def player1():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

def player2():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

def main():

    print("==== Dice Roller Simulator ====")

    while True:
        p1 = player1()
        sum1 = p1[0] + p1[1]

        p2 = player2()
        sum2 = p2[0] + p2[1]

        choice = input("\nWanna roll the dice 🎲? (y/n): ").lower()

        if choice == 'y':
            enter1 = input("Player1 - Press Enter ↲---")
            print(f"Dice1: {p1[0]}")
            print(f"Dice2: {p1[1]}")

            enter2 = input("Player2 - Press Enter ↲---")
            print(f"Dice1: {p2[0]}")
            print(f"Dice2: {p2[1]}")

            print(f"\nPlayer1 scored: {sum1}")
            print(f"Player2 scored: {sum2}")

            winner = 'Player1' if sum1 > sum2 else 'Player2'
            print(f"✨ Winner: {winner}")

        elif choice == 'n':
            print("Exiting the simulator.")
            break

        else:
            print("❌ Invalid choice.")

if __name__ == '__main__':
    main()