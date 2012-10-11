#Exercise 20: Functions and Files

from sys import argv

script, input_file = argv

# prints the data in the file
def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

# prints a single line, takes the line and the file as args
def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file: \n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
current_line = 1 #set the line to the first
print_a_line(current_line, current_file)
print_a_line(2, current_file) #or we can manually choose the line
current_line = current_line + 2
print_a_line(current_line, current_file) #reusing our initial variable
#prints the first three lines of the file
