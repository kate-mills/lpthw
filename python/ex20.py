# provides access to cmd-line args
from sys import argv

# set script, input_file  equal to argv
script, input_file = argv

# set current_file equal to
current_file = open(input_file)


# open and print a file
def print_all(f):
    print f.read()

# go to the very beginning of a file
def rewind(f):
    f.seek(0)

# prints one line of a file
def print_a_line(line_count, f):
    # comma at end of line keeps totlal file from double-spacing
    print line_count, f.readline(),



print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)



print "Let's print three lines:\n"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1

print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
