#Exercise 35: Branches and Functions

from sys import exit
prompt = ">"

def gold_room():
    print "This room is full of gold. How much do you take?"

    next = raw_input(prompt)
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn how to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear in here!"
    print "The bear has a bunch of honey"
    print "The fat bear is infront of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input(prompt)
        if next == "take honey":
            dead("The bear looks at you then slaps your face off!")
        elif next == "taunt the bear" and not bear_moved:
            dead("The bear gets pissed off and chews your leg off")
            bear_moved = True
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "Make a better choice- take honey or taunt the bear"

def cthulhu_room():
    print "Here you see the great evil cthulhu."
    print "He, it, whatever stares at you and you go insane!"
    print "Do you flee for your life or eat your head?"

    next = raw_input(prompt)

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good Job!"
    exit(0)

def start():
    print "You are in a dark room"
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input(prompt)

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room
    elif "gold" or "prize" or "money" in next:
        gold_room()
    else:
        dead("You stumble around the room until your dead")

start()