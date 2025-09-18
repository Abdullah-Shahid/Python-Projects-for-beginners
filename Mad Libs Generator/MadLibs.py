def template(name: str, age: int, job: str) -> str:
    story = f"My name is {name} and I'm {age} years old. Baically I'm an alein from chocgchi planet. There my job was to remove the water from the beach but on EARTH, I'm {job}."

    return story

def main():
    name = input("What's your name: ").capitalize().strip()
    age = int(input("What's your age: "))
    job = input("What's your job/profession: ").capitalize().strip()
    silly_paragraph = template(name, age, job)
    print(silly_paragraph)

if __name__ == '__main__':
    main()