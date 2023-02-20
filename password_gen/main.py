import random


def character():
    random_character = chr(random.randint(ord('a'), ord('z')))
    return random_character


def generate_password():
    password = ""
    for i in range(10):
        password += character()
    return password


if __name__ == '__main__':
    print(generate_password())
