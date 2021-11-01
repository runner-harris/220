def encode(x, key):
    acc = ' '
    for c in x:
        i = ord(c) + key
        acc += chr(i)
    return acc


def encode_better(x, pad):
    acc = " "
    for i in range(len(x)):
        c = ord(x[i])
        key = ord(pad[i % len(pad)])
        new = c + key - 97
        acc += chr(new)
    return acc
