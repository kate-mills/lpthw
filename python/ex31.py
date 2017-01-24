def bear_room():
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off.  Good job!"
    elif bear == "2":
        print "The bear eats your legs off.  Good job!"
    else:
        print "Well, doing %s is probably better.  Bear runs away." % bear

def abyss_room():
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

def gambling_room():
    print "You see a pile of money and pair of dice. What do you do?"
    print "1. Take the money and run!"
    print "2. Roll the dice!"
    print "3. Leave."

    casino = raw_input("> ")

    if casino == "1" or casino == "3":
        print "Scared..."
        abyss_room()
    else:
        print "Not an option!"


print "You enter a dark room with three doors.  Do you go through door #1, door #2, or door #3?"

door = raw_input("> ")

if door == "1":
    bear_room()

elif door == "2":
    abyss_room()

elif door == "3":
    gambling_room()

else:
    print "You stumble around and fall on a knife and die.  Good job!"
