print "\n"
print "\tAsking Questions\n"

print "How old are you?",
age = int(raw_input())
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %d old, %r tall and %r heavy." % (age, height, weight)
print "\n" * 2
print """
We put a ',' at the end of each'print' line.
  This is so the line doesn't end with a newline
  character and go to the next line.
"""
