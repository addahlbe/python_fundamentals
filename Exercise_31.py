#Exercise 31: Making Decisions

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"
prompt = ">"
door = raw_input(prompt)

if door == "1" or "#1" or "one" or "1.":
    print "There's a giant bear here eating cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input(prompt)

    if bear == "1" or "#1" or "one" or "1.":
        print "The bear eats your face off."
    elif bear == "2" or "#2" or "two" or "2.":
        print "The bear eats your leg off."
    else:
        print "Well, that %s was a good call. The bear runs away!" % bear

elif door == "2" or "#2" or "two" or "2.":
    print "You find yourself at the edge of a cliff"
    print "1. take the jump. "
    print "2. turn back. "

    insanity = raw_input(prompt)

    if insanity == 1 or 2:
        print "You wake up from your dream!"
    else:
        print "Splat, you hit the ground!"

else:
    print "You stumble around and fall on a knife and die. Good Job!"

