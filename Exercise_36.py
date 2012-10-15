#Exercise 36: Designing and Debugging

# Use a while loop to loop forever and see what happens
i = 0
bol = True
while bol:
    i = i + 1
    print i
    if i < 100:
        bol = True
    else:
        bol = False
# Delete the else to loop forever
