#Exercise 45: You Make A Game

# TODO: Make a Game
# Use more than one file, and use import to use them.
# Use one class per room and give the classes names that fir their purpose.

from sys import exit
import Exercise_45_functions
from random import randint
prompt = ">"
class Game(object):
    # sets initial room passed to start
    def __init__(self, start):
        self.start = start
    #initializes the next room as start
    # continues to get the next room as play goes on
    def play(self):
        next_room = self.start
        while True:
            print "\n----------"
            room = getattr(self, next_room)
            next_room = room()

    def death(self):
        print "You crops die, you make 0 profit!"
        exit(1)

    def farm(self):
        print "You're an Iowan Farmer, and everything is going great. Until. . ."
        rand = randint(1,3)

        if(rand == 1):
            print "Your crops begin to wilt because it has not rained in a month!"
            print "What would you do?"
            print "Set up a levee: \'levee\'"
            print "Water them with a hose: \'water\'"
            print "Harvest early: \'harvest\'"
            action = raw_input(prompt)
            if action == "levee":
                print "The perfect idea efficeintly gets water to your crops at low cost!"
                Exercise_45_functions.big_increase()
                return 'income'
            if action == "water":
                print "Your crops live on another day!"
                Exercise_45_functions.small_increase()
                return 'farm'
            if action == "harvest":
                print "You make a small profit because your crops have not grown fully."
                Exercise_45_functions.small_increase()
                return 'farm'

        if(rand == 2):
            print "Your crops become infested with pests!"
            print "What would you do?"
            print "Harvest early: \'harvest\'"
            print "Call in an Air-pesticide strike: \'air strike\'"
            print "Have faith in you anti-pest seeds to fight them off \'faith\'"
            action = raw_input(prompt)
            if action == 'harvest':
                print "The buyer notices the pests and doesn't buy them!"
                return 'death'
            if action == 'air strike':
                print "The stike costs a little, but saves all your crops!"
                Exercise_45_functions.small_increase()
                return 'income'
            if action == 'faith':
                print "Some of your crops fight off the pests, but a large percent die."
                Exercise_45_functions.small_decrease()
                return 'farm'

        if(rand == 3):
            print "Heavy rain causes your fields to flood and your crops begin to drown"
            print "What would you do?"
            print "Set up drians \'drain\'"
            print "Hope the weather changes \'hope\'"
            print "Levee the water in a different direction \'levee\'"
            action = raw_input(prompt)
            if action == 'drain':
                print "You waste thousands of gallons of water!"
                print "As you water your crops in the future you pay double!"
                Exercise_45_functions.big_decrease()
                return 'farm'
            if action == 'hope':
                print "The water subsides"
                print "You begin to think what-if and plan for future storms."
                Exercise_45_functions.big_increase()
                return 'farm'
            if action == 'levee':
                print "The water subsides because storm stops."
                print "However you are now prepared for future rain storms"
                Exercise_45_functions.small_decrease()
                return 'farm'
            else:
                print "failed to recognize random"
                return 'death'


    def income(self):
        print "you make $%r on crops!" % (Exercise_45_functions.income)
        exit(1)

a_game = Game("farm")
a_game.play()