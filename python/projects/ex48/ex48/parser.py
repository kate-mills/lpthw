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
    # does not remove from word_list just looks at next_word
    if word_list:
        current_word = word_list[0]
        word_type = current_word[0]
        if (word_type == 'error'):
            print current_word[0]
            return current_word[0]
        else:
            return current_word[0]
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
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")


def parse_sentence(word_list):
    p = lexicon.scan(word_list)
    subj = parse_subject(p)
    verb = parse_verb(p)
    obj = parse_object(p)

    return Sentence(subj, verb, obj)


x = parse_sentence("Princess run North")

print x.subject, x.verb, x.object
