from prac_08_inheritance.unreliable_car import UnreliableCar

unreliable_car = UnreliableCar("Proton", 100, 10)

while unreliable_car.fuel != 0:
    print(unreliable_car)
    unreliable_car.drive(20)
print(unreliable_car)