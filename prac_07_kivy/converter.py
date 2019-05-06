from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

MILES_TO_KM = 1.609344

class ConverterApp(App):

    message = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("converter.kv")
        return self.root

    def convert_to_kilometres(self, miles=0.0):
        try:
            kilometres = float(miles) * MILES_TO_KM
            self.root.ids.kms.text = str(kilometres)
        except ValueError:
            self.root.ids.kms.text = "0.0"

    def handle_increment(self, number=0):
        try:
            self.message = str(float(self.root.ids.miles.text) + number)
        except ValueError:
            self.message = "0.0"
            self.message = str(float(self.root.ids.miles.text) + number)

ConverterApp().run()