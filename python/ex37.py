lan_list = ['javascript', 'python', 'html', 'css']
aTuple = (123, 'xyz', 'zara', 'abc')
another_lan_list = ['c', 'c++', 'c#']

print len(lan_list)  # returns length of list '4'
print max(lan_list)  # returns item with max value  'python'
print min(lan_list)  # returns item with min value  'css'
print list(aTuple)   # converts a tuple to a list


lan_list.append('python')               # appends value to end of list

# extends list by appending contents of another list
lan_list.extend(another_lan_list)
# ['javascript', 'python', 'html', 'css', 'python', 'c', 'c++', 'c#']
print lan_list

# returns count of how many times 'python' occurs in list
py_count = lan_list.count('python')
print 'py_count', py_count

# returns the lowest index in list that 'python' appears
hold_index = lan_list.index('python')
print 'hold_index: ', hold_index

lan_list.insert(2, 'Python')            # inserts 'Python' at index 2


print another_lan_list.pop(-1)  # c      # Removes and returns last object
print another_lan_list.pop(1)  # c++
print another_lan_list.pop(0)  # c


lan_list.remove('c#')                    # Removes 'c#' from list
print lan_list

lan_list.reverse()                      # Reverses objs of list in place
print lan_list


# Sorts objects of list, use compare func if given
lan_list.sort()
print lan_list


ten_things = "Apples Oranges Crows Telephone Light Sugar"

stuff = ten_things.split(' ')           # string to list
new_stuff = ' '.join(stuff)             # list to string
index_three_five = '#'.join(stuff[3:5])  # list to string

print new_stuff, index_three_five, type(new_stuff)
# list_of_nums = range(0, 11, 1) # start, stop, step

# for i in list_of_nums:
#     print i
#
# print list_of_nums[0:4]
