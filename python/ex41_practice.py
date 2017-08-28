def class_is_a(cl_name, par_cl):
  print "Make a class named %s that is-a %s." % (cl_name, par_cl), "\n"
  return cl_name


Twine = class_is_a('Twine', 'Basket')
Sticks = class_is_a('Sticks', 'Basket')


def class_has_a(cl_name, fn_name, s, parms):
  print "class %s(object): def %s(%s, %s)" % (cl_name, fn_name, s, parms)
  print "class %r has a function named %s that takes %s and %s parameters." % (cl_name, fn_name, s, parms), "\n"


class_has_a(Twine, '__init__', 'self', 'weave_type')
class_has_a(Sticks, 'make_stick_fig', 'self', 'length')


def set_to_class(var_name, cl_name):
  print "%s = %s()" % (var_name, cl_name)
  print "Set %s to an instance of class %s" % (var_name, cl_name), "\n"


set_to_class('t', 'Twine')


def get_fun_from_cl(cl_name, fun_name, param1, param2):
  print "%s.%s(%s)" % (cl_name, fun_name, param2)
  if param1 == 'self':
    print "From %s get the %s function, and call it with parameters %s, %s" % (cl_name, fun_name, param1, param2), "\n"
  else:
    print "param1 needs to be self not %s" % (param1)


get_fun_from_cl('practice', 'doing_something', 'self', 'pink')
get_fun_from_cl('practice', 'doing_something', 'oops', 'pink')


def set_an_attribute(cl_name, att_name, set_name):
  print "%s.%s = %s" % (cl_name, att_name, set_name)
  print "From %s get the %s attribute and set it ito %s" % (cl_name, att_name, set_name)


set_an_attribute('foo', 'K', 'Q')
