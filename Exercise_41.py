#Exercise 41: learning to speak object oriented

# class: tell python to make a new kind of thing
# object: two meanings: the most basic kind of thing, and any instance of some thing/class.
# instance: what you get when you tell Python to create a class.
# def: how you define an instance inside a class
# self: inside the functions in a class,self is a varianble for the instance / object being accessed.
# inheritance: the concept that on class can inherit traits from another class, much like you and your parents.
# composition: the concep that a class can be composed of othe classes as parts, much like how a car had wheels.
# attribute: a property classes have that are from composition and are usually variables.
# is-a: A phrase to say that something inherits from another, as in a Salmon is-a Fish.
# has-a: A phrase to say that something is composed of other things or has a trait, as in a salmon has-a mouth.

# Make a class name X that is-a Y 
# class X(Y):

# class Z has-a__init__that takes self and j parameters
# class Z(object):
#     def __init__(self, j):

# class Y has-a function named M that takes self and J parameters.
# class Y(object):
#     def M(self, j):

# Set foo to in instance of class x
# foo = X(): 

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class ###(###):":
      "Make a class named ### that is-a ###.",
    "class ###(object):\n\tdef __init__(self, ***)" :
      "class ### has-a __init__ that takes self and *** parameters.",
    "class ###(object):\n\tdef ***(self, @@@)":
      "class ### has-a function named *** that takes self and @@@ parameters.",
    "*** = ###()":
      "Set *** to an instance of class ###.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("###"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("###", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input("> ")
            print "ANSWER:  %s\n\n" % answer
except EOFError:
    print "\nBye"