from prac_08_inheritance.silver_service_taxi import SilverServiceTaxi

fancy_taxi = SilverServiceTaxi("Fancy Taxi", 200, 2)

fancy_taxi.start_fare()
print(fancy_taxi)
fancy_taxi.drive(18)
print(fancy_taxi)
print("Fare: ${:.2f}".format(fancy_taxi.get_fare()))
