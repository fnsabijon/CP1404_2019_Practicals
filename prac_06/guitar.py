from prac_06.guitar_class import Guitar

def main():
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("tanglewood", 1900, 1552))

    print("These are my guitars:")
    for guitar_number, guitar in enumerate(guitars):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print("Guitar {}: {} ({}), worth ${} {}".format(guitar_number + 1, guitar.name, guitar.year, guitar.cost, vintage_string))

if __name__ == '__main__':
    main()