import random

options = ['Rock', 'Paper', 'Scissor']

def computer_choice():
    global options
    choice = random.choice(options)
    return choice

def main():
    print("==== ROCK PAPER SCISSOR Game ====")

    comp_choice = computer_choice()
    user_choice = input("Enter your choice: ").capitalize()

    print(f"Computer chose {comp_choice}")
    print(f"You chose {user_choice}")

    if comp_choice == user_choice:
        print("Match Tie!")

    elif (comp_choice == 'Rock' and user_choice == 'Scissor' 
          or comp_choice == 'Paper' and user_choice == 'Rock' 
          or comp_choice == 'Scissor' and user_choice == 'Paper'):
        
        print("Computer won.")
        print("You lose.")

    else:
        print("You won.")
        print("Computer lose.")
    
if __name__ == '__main__':
    main()