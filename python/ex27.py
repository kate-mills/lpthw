truth_terms = """
    and
    or
    not
    != (not equal)
    == (equal)
    >= (greater-than-equal)
    <= (less-than-equal)
    True
    False
"""

truth_tables = """

(Is True?)
- NOT -
not False   # True
not True    # False

(Is True?)
- OR -
True or False   # True
True or True    # True
False or True   # True
False or False  # False


(Is True?)
- AND -
True and False  # False
True and True   # True
False and True  # False
False and False # False


(Is True?)
- NOT OR -
not(True or False)  # False
not(True or True)   # True
not(False or True)  # False
not(False or False) # True


(Is True?)
- NOT AND -
not(True and False)  # True
not(True and True)   # False
not(False and True)  # True
not(False and False) # True


(Is True? not equal to )
!=
1 != 0  # True
1 != 1  # False
0 != 1  # True
0 != 0  # False


(Is True? equal to )
== 
1 == 0  # False
1 == 1  # True
0 == 1  # False
0 == 0  # True
"""
print truth_terms
print truth_tables
