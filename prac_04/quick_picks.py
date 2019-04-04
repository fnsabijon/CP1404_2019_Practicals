import random

NUMBER_OF_DRAWS = 6
MIN = 1
MAX = 45


def main():

    number_of_picks = int(input("How many picks? "))

    for i in range(number_of_picks):
        picks = []
        for j in range(NUMBER_OF_DRAWS):
            number = random.randint(MIN, MAX)
            if number in picks:
                number = random.randint(MIN, MAX)
            picks.append(number)
        picks.sort()
        print(picks)


main()


