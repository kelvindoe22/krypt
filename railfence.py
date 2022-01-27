def encrypt(message: str, rails: int):
    a = []
    for i in range(rails):
        a.append([])
    control = 0
    set_num = 0
    for i in message:
        if set_num == rails - 1:
            a[set_num].append(i)
            set_num -= 1
            control = 1
            continue
        elif set_num == 0:
            a[set_num].append(i)
            set_num += 1
            control = 0
            continue
        
        a[set_num].append(i)
        if control:
            set_num -= 1
        else:
            set_num += 1

    encrypted = ""
    
    for i in a:
        encrypted += "".join(i)
    
    return encrypted