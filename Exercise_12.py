#Exercise 12: Prompting People!

#You can also put in a prompt to show to a person so they know what to type. Put a string that
# you want for the promt inside the ()
name = raw_input("Name? ")
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")

print "Hello %r. I see you are %r years old, %r tall, and %r heavy. Nice to meet you." % (name, age, height, weight)
