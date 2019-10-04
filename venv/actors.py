import random

class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature {} of level {}".format(
            self.name,
            self.level

        )
    def get_defensive_roll(self):
        return random.randint(1,12) * self.level


class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level= level

    def attack(self, creature):
        print('{} draws his wand and attacks {}'.format(self.name, creature.name))

        my_roll = random.randint(1,11) * self.level
        #creature_roll = random.randint(1,12) * creature.level
        creature_roll = creature.get_defensive_roll()

        print('You roll {}..'.format(my_roll))
        print('{} rolls {}'.format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print('Harry has won this time')
            return True
        else:
            print('Our young wizard has fallen')
            return False

