i = 0
numbers = []

while i < 6:
  print "At the top i is %d" % i
  numbers.append(i)

  i += 1
  print "Numbers now: ", numbers
  print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
  print num


def list_maker1(stop_num, step):
  i = 0
  numbers = []

  while i < stop_num:
    print "At the top i is %d" % i
    numbers.append(i)

    i += step

    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

  print "The numbers: "

  for num in numbers:
    print num


def list_maker2(start_num, stop_num, step):

  numbers = range(start_num, stop_num, step)
  print "list_maker2: "
  print numbers


list_maker1(4, 2)
list_maker2(0, 10, 3)
