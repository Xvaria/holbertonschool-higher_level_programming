def islower(c):
    l = ord(c)
    if l >= 65 and l <= 90:
        return False
    elif l >= 97 and l <= 122:
        return True
