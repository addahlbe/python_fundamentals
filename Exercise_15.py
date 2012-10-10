#Exercise 15: Reading Files

from sys import argv
# you have to send the argument you want to pass with the file
# ex. python Exercise_15.py Exercise_15_sample.txt
script, filename = argv
prompt = ">"

# we open the file we got passed through argv
    # run pydoc open to see how open works
file = open(filename) 

print "Here's your file %r:" % filename
# call the function read on the file (file) we got
# Do read command with no parameters
file_data = file.read()
print file_data

print "Type the filename again:"
file_again = raw_input(prompt)
# this file has to be in the current directory
txt_again = open(file_again)

print txt_again.read()