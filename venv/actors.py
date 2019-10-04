

class Creature:
    def __init__(self, Name, Level):
        self.name = Name
        self.level = Level

    def __repr__(self):
        return "Creature {} of level {}".format(
            self.name,
            self.level

        )

class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level= level

