from sys import argv
from os.path import exists

# set script, from_file, to_file equal to argv > will be entered on cmd line
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)
# set variable indata equal to a function that opens a file and reads it
indata = open(from_file).read()
# in_file = open(from_file)
# indata = in_file.read()


#in_file = open(from_file)
#indata = in_file.read()

# format the integer-data and set it equal to the length of indata
print "The input file is %d bytes long" % len(indata)

# format the raw-data and set it equal to the Boolean function exists(to_file)
print "Does the output file exist? %r" % exists(to_file)


print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# set out_file equal to a function that opens a file in write mode
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
# in_file.close()
