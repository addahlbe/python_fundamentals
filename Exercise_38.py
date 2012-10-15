#Exercise 38: Doing Things to lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait ther's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
print stuff
more_stuff = ["day", "night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "The're %d items now." % len(stuff)

print "There we go:", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])