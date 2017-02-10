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




def parse_verb(word_list):
    next_word = peek(word_list)
    list_length = len(word_list)
    skip(word_list, 'stop')
    print "46-Verb", next_word, list_length

    if next_word == 'noun':
        skip(word_list, 'noun')
    elif next_word == 'verb':
        return match(word_list, 'verb')
    elif next_word == 'error':
        print "53-Verb found error, peeking at next_word", next_word
        word_list[0] = ('verb', 'die')
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(word_list):
    list_length = len(word_list)
    next_word = peek(word_list)

    print "Object next please:%r%r" %(next_word, list_length)

    if len(word_list) == 0:
        return ('object', 'error0')

    elif not(next_word == 'noun' or next_word == 'direction'): # not True or True = False
        return match(word_list, next_word)
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list):
    list_length = len(word_list)
    next_word = peek(word_list)

    if list_length >= 4:
        skip(word_list, 'stop') # I am ok with stop words being discarded this word being discarded totally
    else:
        if (next_word == 'noun'):
            return match(word_list, 'noun') # If next word is a noun then I found a match
        elif next_word == 'error': # If next word is an error then switch it to player
            word_list[0] = ('noun', 'player')
            return match(word_list, 'noun')
        elif next_word == 'verb':
            return ('noun','player')
        else:
            raise ParserError("Expected a verb next.")


def parse_sentence(word_list):
    p = lexicon.scan(word_list)
    subj = parse_subject(p)
    verb = parse_verb(p)
    obj = parse_object(p)

    return Sentence(subj, verb, obj)


x = parse_sentence("Princess running norths")

print x.subject, x.verb, x.object
