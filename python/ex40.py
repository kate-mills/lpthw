import mystuff

# dict
mystuff_dict = {'apple': 'I AM APPLES', 'tangerine': 'Living Reflection'}
print "dictionary example: "
print "\t%s %s" % (mystuff_dict['apple'], mystuff_dict['tangerine']), "\n"


# module
print "module example: "
print "\t %s %s" % (mystuff.apple(), mystuff.tangerine), "\n"


# class
thing = mystuff.MyStuff()
print "class example: "
print "\t", thing.tangerine, thing.apple(), "\n"


# class
happy_bday = mystuff.Song(["Happy birthday to you",
                           "I don't want to get sued",
                           "So I'll stop right there"])

bulls_on_parade = mystuff.Song(["They rally around the family",
                                "With pockets full of shells"])


print "another class example: ", "\n"


happy_bday.sing_me_a_song(),
bulls_on_parade.sing_me_a_song()
