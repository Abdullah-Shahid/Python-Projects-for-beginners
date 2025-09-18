import random

def word_to_guess():
    words_list = ["python", "lieutenant", "apple", "grapes"]
    word = random.choice(words_list)
    return word


def main():
    print("==== 🎮 Welcome to Hangman! ====")
    guessed_letters = []
    word = word_to_guess()
    attempts = 6

    while attempts > 0:
        display = ""

        for letter in word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"

        print(f"\nWord: {display}")

        if "_" not in display:
               print(f"🎉 You guessed the word! You win!")
               break       
                
        user_guess = input("Guess the letter: ").lower()

        
        if len(user_guess) == 1:

            if user_guess in guessed_letters:
                print("⚠️ You already guessed that letter.")
            
            elif user_guess in word:
                print("✅ Good guess!")
                guessed_letters.append(user_guess)
            
            else:
                guessed_letters.append(user_guess)
                print("❌ Wrong guess.")
                attempts -= 1
                print(f"{attempts} attempts left.")
        
        else:
            print("Guess the letter please.")


        if attempts == 0:
            print(f"\n😢 Game over! The word was '{word}'.")
            break

if __name__ == '__main__':
    main()
    

