#Exercise 32: Loops and Lists

#Examples of lists
hairs = ['brown', 'blond', 'black', 'red', 'brunette', 'funky']
eyes = ['blue', 'brown', 'green']
weights = [1, 2, 3, 4]

for number in weights:
    print "The number is %d" % number

for color in hairs:
    print "A hair of type: %s" % color

for eye in eyes:
    print "Eye color: %s " % eye

#empty list
elements = []

for i in range(0, 6):
    print "adding %d to the list" % i
    elements.append(i)

for i in elements:
    print "Element: ", i    