#Exercise 28: Boolean Practice


def t():
    print "Should be True"
def f():
    print "Should be False"

print True and True
t()

print False and True
f()

print 1 == 1 and 2 == 1
f()

print "test" == "test"
t()

print 1 == 1 or 2 != 1
t()

print True and 1 == 1
t()

print "test" == "testing"
f()

print 1 != 0 and 2 == 1
f()

print "test" != "testing"
t()

print "test" == 1
f()

print not(True and False)
t()

print not( 1 == 1 and 0 != 1)
f()

print (10 == 1 or 1000 == 1000)
t()

print (1 != 10 or 3 == 4)
t()

