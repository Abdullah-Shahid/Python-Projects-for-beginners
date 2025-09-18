import string
import random


def main():
    raw = ""

    print("==== Password Generator ====")
    length = int(input("Length of the password: "))

    if length >= 8:
       print("1. Letters")
       print("2. Digits")
       print("3. Symbol")
       print("4. Exit")

       while True:
           pass_set = int(input("Pick the password set or exit: "))

           if pass_set == 1:
               raw += string.ascii_letters
           elif pass_set == 2:
               raw += string.digits
           elif pass_set == 3:
               raw += string.punctuation
           elif pass_set == 4:
               break
           else:
               print("Invalid set.")

       password = ""
       for i in range(length):
           password += random.choice(raw)

       print(f"Password:\n{password}")

    else:
        print("Password must contain 8 characters (minimum).")

if __name__ == '__main__':
    main()