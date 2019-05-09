from prac_08_inheritance.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness=1.0):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        return "{} plus flagfall of {:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        return super().get_fare() + self.flagfall
