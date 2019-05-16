from prac_08_inheritance.taxi import Taxi
from prac_08_inheritance.silver_service_taxi import SilverServiceTaxi


MENU = "q)uit, c)hoose taxi, d)rive"
CHOICE_PROMPT = ">>> "
BILL_TO_DATE = "Bill to date: ${:.2f}"

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0
    print("Lets Drive!")
    print(MENU)
    choice = input(CHOICE_PROMPT).upper()

    while choice != "Q":
        if choice == "C":
            display_taxis(taxis)
            current_taxi = taxis[int(input("Choose taxi: "))]
            print(BILL_TO_DATE.format(bill_to_date))

        elif choice == "D":
            distance = int(input("Drive how far? "))
            current_taxi.start_fare()
            current_taxi.drive(distance)
            bill_to_date += current_taxi.get_fare()
            print("Your {} trip cost you: ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
            print(BILL_TO_DATE.format(bill_to_date))
        else:
            print("invalid menu")
        print(MENU)
        choice = input(CHOICE_PROMPT).upper()

def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


if __name__ == '__main__':
    main()
