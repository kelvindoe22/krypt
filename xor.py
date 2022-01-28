import random

def encrypt(word: str):
    random.seed(69420)

    a = list(word)
    letters = list(map(ord, a))

    val = ""
    for i in letters:
        val += chr(i ^ random.randint(0,9))
    
    return val

def decrypt(word: str):
    random.seed(69420)
    val = ""
    for i in word:
        val += chr(ord(i) ^ random.randint(0,9))
    
    return val