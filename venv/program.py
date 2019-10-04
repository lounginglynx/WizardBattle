from actors import Wizard, Creature
import random
import time

def main():
    header()
    intro()
    gameLoop()

def header():
    print('---------------------------------------------')
    print('           Wizard Wars')
    print('---------------------------------------------')
    print()

def intro():
    print()
    print('A long time ago in a galaxy far far away.....')
    print('We find our young wizard wandering the enchanted forest')

def gameLoop():
    creatures = [
        Creature('toad', 1),
        Creature('Griffin',50),
        Creature('Yeti',25),
        Creature('Voldemort',1000)
    ]
    hero = Wizard('Harry', 75)
    #print(creatures)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from the mist'.format(active_creature.name,active_creature.level))
        print()

        cmd = input("Do you [a]ttack, [r]un away, or [l]ook around?")
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('Harry runs off to the bushes to recuperate..')
                time.sleep(10)
                print('After finding some butterbeer harry returns stronger then ever')
        elif cmd == 'r':
            print('Harry sprints off into the woods')
        elif cmd == 'l':
            print('Harry looks into the foggy evening and sees:')
            for c in creatures:
                print('A {} of level {}'.format(c.name, c.level))
                print()
        else:
            print('Harry decides he has had enough. And so he reaches around to his back pocket and pulls out a mysterious brown packet')
            print('He flings out a magic bean and throws it into the earth. Quickly he scampers up the fast growing beanstalk to saftey')
            break

        if not creatures:
            print('Our young wizard has beaten the odds and survived the forest')
            break




if __name__ == '__main__':
    main()