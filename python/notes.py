# Reading a file one line at a time
from sys import argv

# python notes.py testing_stuff.txt 
script, my_file = argv

f = open(my_file, 'r')

for line in f:
    print line

f.close
