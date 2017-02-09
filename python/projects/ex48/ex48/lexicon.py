lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',

    'go': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'run': 'verb',

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

        # if word is not in lexicon, add it.
        if not(word in lexicon):
            lexicon[word] = 'error'
            pair = (lexicon[word], word)

        # if value in lexicon is not 'number' and value in lexicon is not 'error'
        if (lexicon[word] != 'number' and lexicon[word] != 'error'):
            pair = (lexicon[word], word)

        else: # word must be a number or error
            num_or_err = convert_number(word)
            pair = (lexicon[word], num_or_err )

        result.append(pair)

    return result
