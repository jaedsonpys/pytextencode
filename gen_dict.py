import string
from random import choice

characters = string.ascii_letters + string.digits
full_characters = string.printable

def gen():
    dict_char = {}

    for c in full_characters:
        chars = ''.join([choice(characters) for __  in range(2)])
        while chars in dict_char.values():
            chars = ''.join([choice(characters) for __  in range(2)])

        dict_char[c] = chars

    print(f'characters = {dict_char}')


gen()
