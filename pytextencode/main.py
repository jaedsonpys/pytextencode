characters = {
    'a': 'Cu', 'b': 'mD', 'c': 'Lh', 'd': 'tx',
    'e': 'ND', 'f': 'pw', 'g': 'RA', 'h': '2b',
    'i': 'Cv', 'j': 'Eb', 'k': 'x4', 'l': 'rW',
    'm': 'kP', 'n': 'H6', 'o': 'GQ', 'p': 'U4',
    'q': 'Ge', 'r': 'Bs', 's': 'X4', 't': 'ir',
    'u': 'rw', 'v': 'CE', 'w': 'Ar', 'x': '3j',
    'y': 'wK', 'z': 'es', 'A': 'XB', 'B': '79',
    'C': 'Uo', 'D': 'tN', 'E': 'Hp', 'F': 'R8',
    'G': 'vk', 'H': 'pu', 'I': 'kK', 'J': 'oh',
    'K': 'Kz', 'L': 'Ro', 'M': 'Nr', 'N': 'zL',
    'O': 'X6', 'P': 'rP', 'Q': '5x', 'R': 'd5',
    'S': '0f', 'T': '9T', 'U': 'gk', 'V': 'ak', 
    'W': 'pX', 'X': 'Dq', 'Y': 'GH', 'Z': 'vV', 
    '0': 'rQ', '1': 'sw', '2': 'iE', '3': 'b6', 
    '4': '44', '5': '1g', '6': 'ns', '7': 'j7', 
    '8': 'X7', '9': 'Gc', '!': 'Z5', '"': 'Av', 
    '#': 'L7', '$': 'Up', '%': '0I', '&': 'gi', 
    "'": 'xV', '(': 'hn', ')': 'L4', '*': 'TX', 
    '+': 'W3', ',': 'og', '-': 'Te', '.': 'g0', 
    '/': 'NZ', ':': 'uZ', ';': 'ST', '<': 'xS', 
    '=': 'zR', '>': 'up', '?': '7G', '@': 'pW', 
    '[': 'Q7', '\\': 'Vu', ']': 'V8', '^': 'A3', 
    '_': 'qM', '`': 'De', '{': 'ne', '|': 'xd', 
    '}': 'CF', '~': 'D8', ' ': 'yp', '\t': 'DR', 
    '\n': '4k', '\r': 'Jn', '\x0b': '42',
    '\x0c': 'Cy'
}


def get_key_by_value(value: str) -> str:
    for k, v in characters.items():
        if v == value:
            return k


def encode(text: str) -> str:
    encoded_text = ''

    for l in text:
        encoded_text += characters[l]

    return encoded_text
