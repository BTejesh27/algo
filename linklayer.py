def char_stuff(d):
    f, e = 'F', 'E'
    s = f
    for c in d:
        if c == f or c == e:
            s += e
        s += c
    return s + f

def char_unstuff(d):
    f, e = 'F', 'E'
    i, s = 1, ''
    while i < len(d) - 1:
        if d[i] == e:
            i += 1
        s += d[i]
        i += 1
    return s

def bit_stuff(d):
    s = ''
    c = 0
    for b in d:
        s += b
        if b == '1':
            c += 1
            if c == 5:
                s += '0'
                c = 0
        else:
            c = 0
    return s

def bit_unstuff(d):
    s = ''
    c, i = 0, 0
    while i < len(d):
        s += d[i]
        if d[i] == '1':
            c += 1
            if c == 5:
                i += 1
                c = 0
        else:
            c = 0
        i += 1
    return s

mode = input("Enter mode (char/bit): ")
data = input("Enter data: ")

if mode == 'char':
    stf = char_stuff(data)
    print("Stuffed:", stf)
    print("Unstuffed:", char_unstuff(stf))

elif mode == 'bit':
    stf = bit_stuff(data)
    print("Bit Stuffed:", stf)
    print("Bit Unstuffed:", bit_unstuff(stf))

else:
    print("Invalid mode")
