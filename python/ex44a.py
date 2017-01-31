class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass


dad = Parent() # set dad to an instance of class Parent
son = Child() # set son to an instance of class Child

dad.implicit()
son.implicit()
