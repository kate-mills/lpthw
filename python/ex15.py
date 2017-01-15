from sys import argv
# set script and filename equal to argv
script, filename = argv

# making a reference to a file
txt = open(filename)

# using 'raw data' formatter to get contents of variable filename
print "Here's your file %r:" % filename
print txt.read()

txt.close()

print "Type the filename again:",
# set file_again equal to raw_input
file_again = raw_input("> ")
# set text_again equal to open(file_again)
text_again = open(file_again)
print text_again.read()
text_again.close()
