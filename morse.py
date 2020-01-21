# morse.py
# pylint: disable=missing-docstring
MORSE_CODE_DICT = { '' : '',
                    '.-' : 'A',
                    '-...' : 'B',
                    '-.-.' :'C',
                    '-..' : 'D',
                    '.' : 'E',
                    '..-.' : 'F',
                    '--.' : 'G',
                    '....' : 'H',
                    '..' : 'I',
                    '.---' : 'J',
                    '-.-' : 'K',
                    '.-..' : 'L',
                    '--' : 'M',
                    '-.' : 'N',
                    '---' : 'O',
                    '.--.' : 'P',
                    '--.-' : 'Q',
                    '.-.' : 'R',
                    '...' : 'S',
                    '-' : 'T',
                    '..-' : 'U',
                    '...-' : 'V',
                    '.--' : 'W',
                    '-..-' : 'X',
                    '-.--' : 'Y',
                    '--..' : 'Z'
                    }

def decode(message):
    word = message.split("/")
    sentence = [decode_word(s) for s in word]
    return ' '.join(sentence)


def decode_word(message):
    if message == "":
        return ""

    symbols = message.split(" ")
    letters = [MORSE_CODE_DICT[s] for s in symbols]
    return ''.join(letters)
