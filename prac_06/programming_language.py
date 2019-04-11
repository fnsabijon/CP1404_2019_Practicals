class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing.lower() == "dynamic":
            return True

    def __str__(self):
        return "{}, {} typing, Reflection={}, first appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)
