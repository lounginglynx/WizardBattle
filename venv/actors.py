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


class Wizard(Creature):

    def attack(self, creature):
        print('{} draws his wand and attacks {}'.format(self.name, creature.name))

        my_roll = self.get_defensive_roll()
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

class MythicalBeast(Creature):


    def get_defensive_roll(self):
        base = super().get_defensive_roll()
        return base * 1.1

class Dragon(Creature):
    def __init__(self, name, level, scalieness, breathesFire):
        super().__init__(name, level)
        self.scaliness = scalieness
        self.breathesFire = breathesFire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breathesFire else 1
        scale_modifier = self.scaliness/10

        return base_roll*fire_modifier*scale_modifier


