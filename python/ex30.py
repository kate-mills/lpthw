people = 60
cars = 40
trucks = 39

if cars > people/3 and cars > trucks:
    print "We should take the cars.",
    print "%d people will fit in %d cars." % (people, cars)
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "%d is too many trucks." % trucks
elif trucks < cars:
    print "Maybe we could take the trucks.",
    print "We have %d trucks and %d cars." % (trucks, cars)
else:
    print "We still can't decide."


if trucks > cars:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
