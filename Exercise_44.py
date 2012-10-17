#Exercise 44: Inheritance VS. Composition

# First: the implicit actions that happen when you define a function in the parent, but not the child.

class Parent(object):
    def implicit(self):
        print "PARENT implicit()"
class Child(Parent):
    #the use of pass under the child class tells Python that you want an empty block
    #this creates a class named child but says there's nothing we want to define inside it.
    #instead we inherit all of its behavior from parent.
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
print '-' * 20
# Second: The problem with implcitly having functions called is sometimes you want the child to behave differently.
# In this case you want to override the function in the child, effectively replacing the functionality.
# To do this just define a function with the same name in Child!

class Parent2(object):
    def override(self):
        print "PARENT override()"
    def not_override(self):
        print "PARENT-NOT OVERRIDE!"
class Child2(Parent2):
    def override(self):
        print "CHILD override()"
dad = Parent2()
son = Child2()
dad.override()
son.override()
dad.not_override()
son.not_override()
print '-' * 20
# Third: is a special case where you want to alter the behavior before or after you have the parent class's version run.
# You first override the function just like in the last example, but then you use Python built in function named *super*
# to get the Parent version to call.

class Parent3(object):
    def altered(self):
        print "Parent altered()"
class Child3(Parent3):
    def altered(self):
        print "Child before parent altered()"
        super(Child3, self).altered
        print "CHILD after Parent altered()"
dad = Parent3()
son = Child3()
dad.altered()
son.altered()
print '-' * 20
# Fourth: all three combined

class Parent4(object):
    def override(self):
        print "Parent override()"
    def implicit(self):
        print "Parent implicit()"
    def altered(self):
        print "Parent altered()"
class Child4(Parent4):
    def override(self):
        print "Child override()"
    def altered(self):
        print "Child before parent altered()"
        super(Child4, self).altered
        print "CHILD after Parent altered()"
dad = Parent4()
son = Child4()
dad.implicit()
son.implicit()
dad.altered()
son.altered()
dad.override()
son.override()
print '-' * 20
# This should seem like common sense, but then we get into trouble with a thing called Multiple inheritance.
class SuperFun(Child3, Parent):
    pass
double_inheritance = SuperFun()
double_inheritance.implicit()
double_inheritance.altered()
# good example is a snake can inherit from a pet, and a reptile.


