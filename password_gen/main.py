import random


def character():
    random_character = chr(random.randint(ord('a'), ord('z')))
    return random_character


def generate_password(required_length):
    password = ""
    for i in range(required_length):
        password += character()
    return password


if __name__ == '__main__':
    length = int(input("Password Length: "))
    while not 0 < length < 50:
        print("Invalid length. Must be between 0 and 50")
        length = int(input("Password Length: "))
    print(generate_password(length))
