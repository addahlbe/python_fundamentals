#Exercise 34: Accessing Elements of Lists

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
r = len(animals)
print "We have %r animals." % r

bear = animals[0]
python = animals[1]
peacock = animals[2]
kangaroo = animals[3]
whale = animals[4]
platypus = animals[5]

print "The first animal:", bear
print "The second animal:", python
print "The third animal:", peacock
print "The fourth animal:", kangaroo
print "The fifth animal:", whale
print "The sixth animal:", platypus

for i in range(r):
    print "The %d animal is a %s" % (i + 1, animals[i])