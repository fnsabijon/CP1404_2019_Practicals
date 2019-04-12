from prac_06.guitar import Guitar

guitar_1 = Guitar("Gibson", 1950, 10000)
guitar_2 = Guitar("Tanglewood", 1990, 3000)
guitar_3 = Guitar("Taylor", 1968, 5000)

guitars = [guitar_1, guitar_2, guitar_3]

print("Expect gibson, tanglewood, and taylor to be 69, 29, and 51 years old respectively. Only Tanglewood is not vintage")
print("\nTest results:")

for guitar in guitars:
    age = guitar.get_age()
    is_vintage = guitar.is_vintage()
    print("{} is {} years old".format(guitar.name, age))
    if is_vintage:
        print("{} is vintage".format(guitar.name))
    else:
        print("{} is not vintage".format(guitar.name))
