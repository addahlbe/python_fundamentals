#Exercise 17: More Files
# Copies from one file to another file
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long." % len(indata)

print "Does the output file exist? %r" % exists(to_file)

print "Ready? Hit return to continue or Enter CNTRL-C to abort."
raw_input(">")

out_file = open(to_file, 'w')
out_file.write(indata)

print "Complete. . ."

out_file.close()
in_file.close()