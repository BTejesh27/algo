def char_stuff(d):
    f, e = 'F', 'E'
    s = f
    for c in d:
        if c == f or c == e:
            s += e
        s += c
    return s + f


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


mode = input("Enter mode (char/bit): ")
data = input("Enter data: ")

if mode == 'char':
    stf = char_stuff(data)
    print("Stuffed:", stf)

elif mode == 'bit':
    stf = bit_stuff(data)
    print("Bit Stuffed:", stf)

else:
    print("Invalid mode")
