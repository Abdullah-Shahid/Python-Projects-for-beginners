def main():
    questions = {
        "1. How many cards are in a standard deck of playing cards?": [51, 55, 57, 52],

        "2. What is the only planet in our solar system to rotate clockwise on its axis": ['Mercury', 'Venus', 'Neptune', 'Jupiter'],

        "3. What does “URL” stand for?": ['Uniform resource locator', 'Unified resource location', 'Uniform research locator'],

        "4. Which country is the largest in the world?": ['India', 'China', 'UK', 'Russia'],

        "5. What was the first animal to ever be cloned?": ['Sheep', 'Monkey', 'Lion', 'Goat']
    }

    answers = [52, "Venus", "Uniform resource locator", "Russia", "Sheep"]

    score = 0

    while True:
        for question in questions:
            print(question)
            for options in questions[question]:
                print(options)
            user_ans = input("Answer: ").strip()
            if user_ans.lower() in str(answers).lower():
                    print("Correct Answer!")
                    score += 1
            else:
                    print("Wrong Answwer!")
        break          

    print(f"You scored {score} out of {len(questions)}.")


if __name__ == '__main__':
    main()
