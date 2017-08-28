import lexicon


class ParserError(Exception):
  pass


class Sentence(object):

  def __init__(self, subject, verb, obj):
    # remember we take ('noun','princess') tuples and convert them
    self.subject = subject[1]
    self.verb = verb[1]
    self.object = obj[1]


def peek(word_list):
  # ('noun', 'princess') returns 'noun'
  if word_list:
    word = word_list[0]
    return word[0]
  else:
    return None


def match(word_list, expecting):
  if word_list:
    word = word_list.pop(0)

    if word[0] == expecting:
      return word
    else:
      return None
  else:
    return None


def skip(word_list, word_type):
  while peek(word_list) == word_type:
    match(word_list, word_type)


# searches through list of tuples for first error or noun
def parse_subject(word_list):
  skip(word_list, 'stop')
  next_word = peek(word_list)
  if next_word == None:
    return ('noun', 'Wake up!!')
  if next_word == 'error':  # If first word is an error I am overwriting it
    word_list[0] = ('noun', 'player')
    return match(word_list, 'noun')
  elif (next_word == 'noun'):  # If first word is a noun I found a match
    return match(word_list, 'noun')
  # If first word is verb return player so verb is not poped off
  elif next_word == 'verb' or next_word == 'direction':
    return ('noun', 'player')
  else:
    raise ParserError("Expected a verb next.")

# searches through word list for first error or verb or None


def parse_verb(word_list):
  skip(word_list, 'stop')
  next_word = peek(word_list)

  if next_word == None:  # if word_list is empty
    return('verb', 'die')
  elif next_word == 'error':  # error found
    word_list[0] = ('verb', 'die')  # overwrite error
    return match(word_list, 'verb')  # pop it off
  elif next_word == 'noun' or next_word == 'direction':  # noun or direction
    return ('verb', 'die')  # return die
  elif next_word == 'verb':  # verb found
    return match(word_list, 'verb')
  else:
    raise ParserError("Expected a verb next.")


def parse_object(word_list):
  next_word = peek(word_list)
  skip(word_list, 'stop')

  if next_word == None:
    return ('object', 'nothingness')
  elif not(next_word == 'noun' or next_word == 'direction'):  # not True or True = False
    return match(word_list, next_word)
  elif next_word == 'direction' or next_word == 'noun':
    return match(word_list, next_word)
  else:
    raise ParserError("Expected a noun or direction next.")


def parse_sentence(word_list):
  p = lexicon.scan(word_list)
  subj = parse_subject(p)
  verb = parse_verb(p)
  obj = parse_object(p)

  return Sentence(subj, verb, obj)


stuff = raw_input("> ")
x = parse_sentence(stuff)

print x.subject, x.verb, x.object
