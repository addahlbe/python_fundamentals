## Exercise 5: More Variables and Printing

my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74.0
my_weight = 180.0
my_eyes = 'Blue'
my_teeth = 'white'
my_hair = 'Brown'

my_height_centimeters = my_height * 2.54
my_weight_kilos = my_weight * 0.4536

print "Let's talk abot %s." % my_name
print "He's %d inches tall, or %d centimeters tall." % (my_height, my_height_centimeters)
print "He's %d pounds heavy, or %d kilos heavy." % (my_weight, my_weight_kilos)
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee" % my_teeth

print "If I add %d, %d, and %d, I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)