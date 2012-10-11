#Exercise 21: Functions Can Return Something
# function to add three numbers plus 10
def add(a, b, c):
    print "ADDING %d + %d + %d" % (a, b, c)
    return a + b + c 
#function to subtract two numbers
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
#function to multiply two numbers
def multiply(a, b):
    print "MULTIPLY %d * %d" % (a, b)
    return a * b
#function to divide two numbers
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with functions!"

print add(17, 74, 10)
print subtract(10239, 123)
print multiply(12, 12)
print "%d" % subtract(divide(16, 4), add(1, 2, 1))
