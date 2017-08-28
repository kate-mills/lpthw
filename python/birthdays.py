birthdays = {'Shera': 'Feb 6', 'Melissa': 'Jan 28', 'Misty': 'Feb 4'}

while True:
  print('Enter a name: (blank to quit)'),
  name = raw_input('')

  if name == '':
    break

  if name in birthdays:
    print"%s's birthday is %s\n" % (name, birthdays[name])
  else:
    print('I do not have birthday information for ' + name)
    print('What is their birthday?')
    bday = raw_input()
    birthdays[name] = bday
    print('Birthday database updated!')
    print('\n')
