from actors import Wizard, Creature

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
        Creature(),
        Creature(),
        Creature()
    ]
    hero = Wizard()


    while True:
        cmd = input("Do you [a]ttack, [r]un away, or [l]ook around?")
        if cmd == 'a':
            print('Wands Drawn')
        elif cmd == 'r':
            print('Harry sprints off into the woods')
        elif cmd == 'l':
            print('Harry looks around for a good pub')
        else:
            print('Harry decides he has had enough. And so he reaches around to his back pocket and pulls out a mysterious brown packet')
            print('He flings out a magic bean and throws it into the earth. Quickly he scampers up the fast growing beanstalk to saftey')
            break





if __name__ == '__main__':
    main()