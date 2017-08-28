from nose.tools import *
from ex47.game import Room
from ex47.artists import Art


def test_room():
  gold = Room("GoldRoom",
              """This room has gold in it you can grab.  There's a
                door to the north.""")
  assert_equal(gold.name, "GoldRoom")
  assert_equal(gold.paths, {})


def test_room_paths():
  center = Room("Center", "Test room in the center.")
  north = Room("North", "Test room in the north.")
  south = Room("South", "Test room in the south.")

  center.add_paths({'north': north, 'south': south})
  assert_equal(center.go('north'), north)
  assert_equal(center.go('south'), south)


def test_map():
  start = Room("Start", "You can go west and down a hole.")
  west = Room("Trees", "There are trees here, you can go east.")
  down = Room("Dungeon", "It's dark down here, you can go up.")

  start.add_paths({'west': west, 'down': down})
  west.add_paths({'east': start})
  down.add_paths({'up': start})

  assert_equal(start.go('west'), west)
  assert_equal(start.go('west').go('east'), start)
  assert_equal(start.go('down').go('up'), start)


def test_room():
  mark = Art("Annie on Horse",
             "Portrait")
  assert_equal(mark.title, "Annie on Horse")
  assert_equal(mark.category, "Portrait")
  assert_equal(mark.colors, {})


def test_art_colors():
  blue = Art("blue", "Test color blue.")
  red = Art("red", "Test color red.")
  white = Art("white", "Test color  white.")

  blue.add_colors({'white': white, 'red': red})
  assert_equal(blue.paint('white'), white)
  assert_equal(blue.paint('red'), red)


def test_map():
  spring = Art("Spring", "Contains Spring White and Brown.")
  white = Art("White", "Mix with Spring and Brown")
  brown = Art("Brown", "Mix with Spring and White")

  spring.add_colors({'white': white, 'brown': brown})
  white.add_colors({'green': spring})
  brown.add_colors({'hop': spring})

  assert_equal(spring.paint('white'), white)
  assert_equal(spring.paint('white').paint('green'), spring)
  assert_equal(spring.paint('brown').paint('hop'), spring)
