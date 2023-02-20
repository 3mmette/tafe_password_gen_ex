import random


def lower_character():
    random_lower_character = chr(random.randint(ord('a'), ord('z')))
    return random_lower_character


def upper_character():
    random_upper_character = chr(random.randint(ord('A'), ord('Z')))
    return random_upper_character


def number():
    random_number = random.randint(0, 9)
    return random_number


def special_character():
    special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    character = random.choice(special_characters)
    return character


def generate_password(required_length):
    password = ""
    for i in range(required_length):
        character = int(random.randint(1, 4))
        if character == 1:
            password += lower_character()
        elif character == 2:
            password += upper_character()
        elif character == 3:
            password += str(number())
        elif character == 4:
            password += special_character()
        else:
            print("Error")
    return password


if __name__ == '__main__':
    length = int(input("Password Length: "))
    while not 0 < length < 50:
        print("Invalid length. Must be between 0 and 50")
        length = int(input("Password Length: "))
    print(generate_password(length))
