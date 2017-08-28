class Parent(object):
  def __init__(self, name):
    self.name = none

  def override(self):
    print "PARENT override()"


class Child(Parent):

  def override(self):
    print "CHILD override()"


dad = Parent()
son = Child()

dad.override()
son.override()
dad.override()
