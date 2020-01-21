# morse.py
# pylint: disable=missing-docstring

def decode(message):
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

    message_split = message.split(' ')
    result = ""

    for code in range(len(message_split)):
        result += MORSE_CODE_DICT[message_split[code]]
    return result
