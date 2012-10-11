#Exercise 16: Reading and Writing Files
from sys import argv
#Deletes a selected file from the current directory
script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want to delete %r, hit CTRL-C (^C)."
print "If you do want that, type: delete"
print "If you want to view the contents of the file type: view"

def delete(filen):
    print "Deleting file. . ."
    target = open(filen, 'w')
    target.truncate()
    print "File Deleted Sucessfully!"
    print "Closing file. . ."
    target.close()

def write(filen):
    print "Now I'm going to ask you for three lines."
    target = open(filen, 'w')

    line1 = raw_input("Line 1: ")
    line2 = raw_input("Line 2: ")
    line3 = raw_input("Line 3: ")

    print "Writing lines to file. . ."

    target.write(line1)
    target.write("\n")
    target.write(line2)
    target.write("\n")
    target.write(line3)
    target.write("\n")
    print "Complete!"
    target.close()


read = raw_input(">")

if(read == "view"):
    file = open(filename)
    print file.read()
    read2 = raw_input("Delete? (yes/no)")
    if(read2 == "yes"):
        delete(filename)
    else:
        print "File Saved"

if(read == "delete"):
    delete(filename)
    read3 = raw_input("Would you like to add data to the file? (yes/no)")
    if(read3 == "yes"):
        write(filename)
    else:
        print "Complete. . ."    
