class Parent(object):

  def altered(self):
    print "PARENT altered()"


class Child(Parent):

  def altered(self):
    print "CHILD, BEFORE PARENT altered()"
    # super ensures the parent class is looked up corretly
    # whatever parent class Child has, call the altered function from it
    super(Child, self).altered()
    print "CHILD, AFTER PARENT altered()"


dad = Parent()
son = Child()

dad.altered()
son.altered()
