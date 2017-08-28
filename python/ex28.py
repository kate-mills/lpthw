def boolean_test(test_left, operator, test_right, answer):
  print "'AND' + 'False' = FALSE "
  print ""
  test_string = test_left, operator, test_right
  print answer
  print 'hi', str(answer)
  print '\nIs True?...', test_string, answer


print "\nnot (True and False)", not (True and False)  # True
print "\nnot (1 == 1 and 0 != 1)", not (1 == 1 and 0 != 1)  # False

boolean_test(True, 'and', True, True and True)
boolean_test(False, 'and', True, False and True)
boolean_test('1==1', 'and', '2==1', 1 == 1 and 2 == 1)
boolean_test('test', '==', 'test', 'test' == 'test')
boolean_test(True, 'and', '1==1', True and 1 == 1)
boolean_test(False, 'and', '0!=0', False and 0 != 0)
boolean_test(True, 'or', '1==1', True or 1 == 1)
boolean_test('test', '==', 'testing', "test" == "testing")
boolean_test('1!=0', 'and', '2==1', 1 != 0 and 2 == 1)
boolean_test('test', '!=', 'testing', "test" != "testing")
boolean_test('test', '==',  1, "test" == 1)
boolean_test(True, '==', 1, True == 1)
boolean_test(False, '==', 0, False == 0)
# test5 = ("peanuts" and "crackerjacks")
test6 = not("peanuts" and "crackerjacks")
test1 = not(True and False)  # not(True and False) = TRUE
test2 = not("testing" == "testing" and "python" ==
            "Python")  # not(True and False) = TRUE
test3 = not(True and False)  # not(True and False) = TRUE
test4 = not(1 == 1 and 0 != 1)  # not(True and True) = FALSE
boolean_test('not(True', 'and', 'False)', test1)
boolean_test('not("testing=="testing"', 'and', '"python" == "Python")', test2)
# boolean_test("peanuts", "and", "crackerjacks", test5)
print "test6: ", test6
