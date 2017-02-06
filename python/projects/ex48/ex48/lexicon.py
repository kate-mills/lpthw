
lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',

    'go': 'verb',
    'kill': 'verb',
    'eat': 'verb',

    'the': 'stop',
    'in': 'stop',
    'of': 'stop',

    'bear': 'noun',
    'princess': 'noun',

    '1234': 'number',
    '3': 'number',
    '91234': 'number'
}


def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return s.upper()



def scan(paragraph):
    words = paragraph.lower().split()
    result = []

    for word in words:
        #add word to lexicon as an error
        if not(word in lexicon):
            word = word.upper()
            lexicon[word] = 'error'
            pair = (lexicon[word], word)

        if (lexicon[word] != 'number' and lexicon[word] != 'error'):
            pair = (lexicon[word], word)

        else:
            number_or_error = convert_number(word)
            pair = (lexicon[word], number_or_error)

        result.append(pair)

    return result

scanned = scan('IAS 1234 blah raley in migrate South The In ')
print scanned
