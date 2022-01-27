# Doesn't work with spaces :( 

def zip_up(string: str, key: str):
    string = string.lower()
    key = key.lower()
    z = zip(list(string),list(key))
    return list(z)

def make_ascii_lower(tup):
    return chr((((ord(tup[0]) - 97) + (ord(tup[1]) - 97)) % 26) + 97)

def encrypt(message: str, key: str):
    ret_val = ""
    for i in zip_up(message, key):
        ret_val += make_ascii_lower(i)
    return ret_val
