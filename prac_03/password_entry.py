"""Fred Nathaniel Sabijon"""



MIN_LENGTH = 5

def main():
    password = get_password()

    print_asterisks(password)


def print_asterisks(password):
    for char in password:
        print("*", end="")


def get_password():
    password = input("Please enter your password: ")
    while len(password) < MIN_LENGTH:
        password = input("Please enter more than 5 characters: ")
    return password


main()