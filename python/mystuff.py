
def apple():
  return "I AM APPLES!"


tangerine = "Living reflection of a dream."


class MyStuff(object):

  def __init__(self):
    self.tangerine = "And now a thousand years between"

  def apple(self):
    return "I AM CLASSY APPLES!"


class Song(object):
  def __init__(self, lyrics):
    self.lyrics = lyrics

  def sing_me_a_song(self):
    for line in self.lyrics:
      print line
