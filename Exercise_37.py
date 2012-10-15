#Exercise 37: Symbol Review
# use each once to prove you know them!


keywords = ['and','del','from','not','while','as','elif','global','or','with','assert','else','if','pass','yield','break','except',
    'import','print','class','exec','in','raise','continue','finally','is','return','def','for','lambda','try']

#and not or else if
if(2 < 3 and 3 >= 2):
    if(not False or False):
        print "Hello"
    elif(2 > 3):
        print "Wont reach this!"
    else:
        print "Wont reach this either!"     

#del deletes an item from a list
del keywords[0]

#from
#from sys import argsv
#script, input_file = argv
# used to import files, functions, or arguments

# while
x = 0
while x < 6:
    x = x + 1
    print x

# global
globvar = 0
def edit_globvar():
    global globvar
    globvar = 2
def print_globvar():
    print "The global variable equals: ", globvar
print_globvar()
edit_globvar()
print_globvar()

#create a class named fruit.
#an instance of that class (an object) would be a single fruit
#you can have several instances of one class

class fruit:
    #properties(
    fruit = ""
    color = ""
    taste = ""
    # )end properties
    #methods(
    def print_fruit(self):
        print "%s :" % self.fruit
        print self.color
        print self.taste
        # has to be self because what if multiple fruits!
        # self is a reference to the object that is currently being manipulated   

    #)
#methods are functions contained within a class. The diefference is that you put a method inside a class, 
# and it belongs to that class. If you ever want to call that method you have to reference an object
# of that class first, just like the variables.
# KEY! Big difference between method and function is a method always has to have an argument! called
# self between the parentheses.

# a class on its own isnt't something you can directly manipulate: first we have to create
# an instance of the class to play with. You can store the instance in a variable.

#INHERITANCE
class apple(fruit):
    fruit = "apple"
    color = "red"
    taste = "sweet"
    def stem(self):
        print "Have a stem"
class orange(fruit):
    fruit = "orange"
    color = "orange"
    taste = "sour"
    def rhine(self):
        print "Have a rhine"


Apple = apple()
Apple.print_fruit()
Apple.stem()

Orange = orange()
Orange.print_fruit()
Orange.rhine()
