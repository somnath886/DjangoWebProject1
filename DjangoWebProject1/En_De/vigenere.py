def is_valid(s):
    for ch in s:
        if not ch.isalpha():
            return False
    return True

def encrypting(p, k):
    j = 0
    string = []
    failure = 'Only Letters'

    if not is_valid(k):
        return failure

    for ch in p:
        if not ch.isalpha():
            string.append(ch)
            continue

        ascii_offset = 65 if ch.isupper() else 97

        pi = ord(ch) - ascii_offset
        kj = ord(k[j % len(k)].upper()) - 65
        ci = (pi + kj) % 26
        j += 1
        c = chr(ci + ascii_offset)
        string.append(c)

    return ''.join(string)

def decrypting(p, k):
    j = 0
    string = []
    failure = 'Only Letters'

    if not is_valid(k):
        return failure

    for ch in p:
        if not ch.isalpha():
            string.append(ch)
            continue

        ascii_offset = 65 if ch.isupper() else 97

        pi = ord(ch) - ascii_offset
        kj = ord(k[j % len(k)].upper()) - 65
        ci = (pi - kj) % 26
        j += 1
        c = chr(ci + ascii_offset)
        string.append(c)

    return ''.join(string)



    
    



