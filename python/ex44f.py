class Parent(object):
  def override(self):
    print "PARENT override()"

  def implicit(self):
    print "PARENT implicit()"

  def altered(self):
    print "PARENT altered()"


class Child(Parent):

  def __init__(self, stuff):
    self.stuff = stuff
    super(Child, self).__init__()
    print stuff

  def override(self):
    print "CHILD override()"

  def altered(self):
    print "CHILD, BEFORE PARENT altered()"
    super(Child, self).altered()
    print "CHILD, AFTER PARENT altered()"


dad = Parent()
son = Child('I am Child that inherits from Parent')
dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()


class BadStuff(object):
  pass


class Candy(object):
  pass
# make a class named SuperFun that inherits from classes Child and BadStuff
# not a good idea to do this


class SuperFun(Candy, BadStuff):
  pass
