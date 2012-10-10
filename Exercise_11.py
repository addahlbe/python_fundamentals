#Exercise 11: Asking Questions
#read in data through the terminal:
# 1. Go to directory where file is located
# 2. enter- python filename.py
# 3. it should display in terminal


print "How old are you?"
age = raw_input()
print "How tall are you?"
height = raw_input()
print "How much do you weigh?"
weight = raw_input()

print "So, you are %r years old, %r tall and %r heavy? (y/n)" % (age, height, weight)
