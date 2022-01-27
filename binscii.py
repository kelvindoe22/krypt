def encrypt(message: str):
    val = ""
    for i in message:
        val += f"{ord(i):08b} "
    return val[:-1]