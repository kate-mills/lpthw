# Example of inheritance
class Parent(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def print_info(self):
    print self.name, 'is', self.age


class Child(Parent):
  def __init__(self, name, age):
    super(Child, self).__init__(name, age)


dad = Parent('dad', 100)
son = Child('tom', 50)

dad.print_info()
son.print_info()
