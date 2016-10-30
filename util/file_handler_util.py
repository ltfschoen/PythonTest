import random
import string

def random_char(char_qty):
    return ''.join(random.choice(string.ascii_letters) for char in range(char_qty))
