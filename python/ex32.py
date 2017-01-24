the_count = [0, 1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print "This is count %d" % number


for fruit in fruits:
    print "A fruit of type: %s" % fruit


for cell in change:
    print "I got %r" % cell

# build a list - start with empty list
# elements = []
# print "fruits in basket: %r" % len(fruits)
#
# for i in range(0, 6):
#     print "Adding %d to the list." % i
#     elements.append(i)
#
# for i in elements:
#     print "Element was: %d" % i

elements = range(0, 6) #range(start, stop, step) [0, 1, 2, 3, 4, 5]
print elements


for i in elements:
    print "Element was: %d" % i




for i in xrange(0, 11, 2):
    if i == 0:
        pass
    else:
        print("what's up?")


for i in xrange(10):
    print(i)
