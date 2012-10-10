#Exercise 10: What was that?

# print "I "understand" joe." will return an error because the interpreter can't parse the inside string.

print "I \"understand\" joe. \n" #solves the problem using an escape sequence.
print "I am 6'2\"\n" # here is another example

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backlash_cat =  "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print"\n"
print persian_cat
print "\n"
print backlash_cat
print "\n"
print fat_cat

print """
escape sequences:
\t* \\ Backslash
\t* \' Single quote
\t* \" Double quote
\t* \a ASCII Bell
\t* \b ASCII Backspace
\t* \f ASCII formatted
\t* \n ASCII linefeed
\t* \r Carriage return
\t* Look up the rest!
"""

print '''
why is triple quote helpful?
testing it might show you?
or you might never know?
It's a matter of preference! haha!
'''