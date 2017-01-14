print "\n\tStrings and Text"
print "Tutorial on Numbers:\nhttps://www.tutorialspoint.com/python/python_numbers.htm\n"

# Use %d when displaying numbers to users
x = "There are %d types of people." % 10.0
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)

print x
print y

#Use %r for debugging since it displays the 'raw' data of the variable
print "I said: %r." % x
# %s is used to display a string
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
