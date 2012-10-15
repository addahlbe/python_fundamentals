#Run Exercise 25

#First review the example on the web

# you do not need the .py at the end to import it. When you do this you make a module that has all your
# functions in it to use.
import Exercise_25

sentence = "All good things come to those who wait"
# you use the Exercise_25 module and call your first function. The . symbol
# is how you tell python, inside Exercise_25 there's a function called break_words and I want to run it.
words = Exercise_25.break_words(sentence)
print "Words of the sentence: ", words

sorted_words = Exercise_25.sort_words(words)
print "Words of the sentence sorted: ", sorted_words

print "First word of sentence: "
Exercise_25.print_first_word(words)
print "Last word of sentence: " 
Exercise_25.print_last_word(words)

help(Exercise_25)