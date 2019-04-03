
def main():

    total = 0
    number_of_items = int_validation(input("Please enter the number of items: "))
    for i in range(0, number_of_items, 1):
        total += int_validation(input("Please enter price of item: "))

    if total > 100:
        total = total - (total * 0.1)

    print("Total price for", number_of_items, "items is: $" + str(total))


def int_validation(value):
    while value.isnumeric() == False:
        value = input("Please enter a valid number: ")
    return int(value)

main()