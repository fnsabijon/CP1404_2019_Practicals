from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class MyDynamicApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Bob Builder", "Wreckit Ralph", "Fixit Felix"]

    def build(self):
        self.title = "My Dynamic App"
        self.root = Builder.load_file("my_dynamic_app.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            label = Label(text=name)
            self.root.ids.names.add_widget(label)


MyDynamicApp().run()