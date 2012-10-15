#Exercise 33: While Loops
def while_loop(list, value, incrimenter):
    i = 0
    while i < value:
        print "at the top i is %d" % i
        numbers.append(i)

        i = i + incrimenter
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "


numbers = []
value = 10
incrimenter = 2
while_loop(numbers, value, incrimenter)
for num in numbers:
    print num
