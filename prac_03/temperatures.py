MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def convert_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))

def convert_to_celcius():
    global fahrenheit
    fahrenheit = float(input("Fahrenheit: "))
    celcius = 5 / 9 * (fahrenheit - 32)
    print("Result: {:.2f} C".format(celcius))

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            convert_to_fahrenheit()
        elif choice == "F":
            convert_to_celcius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


main()
