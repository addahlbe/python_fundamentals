#Exercise 39: Dictionaries, Oh Lovelety Dictionaries

#python calls them "dicts" other languages call them "hashes"

# What matters is seeing how they are different from lists.
# Lists let you:
things = ['a', 'b', 'c', 'd']
# you use numbers to get things out of a list by index.
print things[1]
# you use numbers to replace things by index.
things[1] = 'z'
print things[1]
print things

# what a dict does is let you usse anything! not just numbers!

#dict
stuff = {'name' : 'Zed', 'age' : 36, 'height' : 6*12+2}
print stuff['name']
print stuff['age']
print stuff['height']
stuff['city'] = "San Francisco"
print stuff['city']
print stuff

stuff[1] = "Wow"
stuff[2] = "Neato"
print stuff[1]
print stuff[2]
print stuff

# delete stuff
del stuff['city']
del stuff[1]
del stuff[2]
print stuff
# Create a mapping of state to abreviation
states = {
    'Oregeon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}
# Create a basic set of states and cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'NY' : 'New York',
    'FL' : 'Jacksonville',
    'OR' : 'Portland'
}
# add some more cities and states
states['Illinois'] = "IL"
cities['IL'] = 'Chicago'
# print out some cities
print '-'*10
print "NY State has", cities["NY"]
print "OR State has", cities["OR"]
#print some states
print '-'*10
print "Illinois abreviation is:", states['Illinois']
print "Floridas abreviation is:", states['Florida']
# print every state abreviation
print '-'*10
for city, abbrev in cities.items():
    print "%s has the city %s" % (city, abbrev)
# print every state 
print '-'*10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)
# now do both at the same time
print '-'*10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry no Texas"
# get a city with default value
city = cities.get('TX', 'Does Not Exists')
print "The city for the state 'TX' is : %s" % city