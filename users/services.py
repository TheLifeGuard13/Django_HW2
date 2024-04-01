import random
import string


def generating_keys(symbols):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=symbols))
