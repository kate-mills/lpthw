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

    skip(word_list, 'stop') #
    next_word = peek(word_list)

    if next_word == 'error': # If first word is an error I am overwriting it
        word_list[0] = ('noun', 'player')
        return match(word_list, 'noun')
    elif (next_word == 'noun'): # If first word is a noun I found a match
        return match(word_list, 'noun')
    elif next_word == 'verb': # If first word is verb return player so verb is not poped off
        return ('noun','player')
    else:
        raise ParserError("Expected a verb next.")

# searches through word list for first error or verb or None
def parse_verb(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'verb': # if first word is 'verb' match it and pop it off
        return match(word_list, 'verb')
    elif next_word == 'error': # user made a mistake w the verb so I am overwriting it
        word_list[0] = ('verb', 'die')
        return match(word_list, 'verb')
    elif next_word == 'noun' or next_word == 'direction': # user left out a verb and next word is object
        return ('die', 'verb')
    elif next_word == None:
        return('verb', 'nothingness')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(word_list):
    next_word = peek(word_list)
    skip(word_list, 'stop')

    if next_word == None:
        return ('object', 'nothingness')
    elif not(next_word == 'noun' or next_word == 'direction'): # not True or True = False
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
