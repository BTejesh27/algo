
def crc_remain(data, poly, fill='0'):
    n = len(poly)
    d = list(data + fill * (n - 1))
    for i in range(len(data)):
        if d[i] == '1':
            for j in range(n):
                d[i + j] = str(int(d[i + j] != poly[j]))
    return ''.join(d[-(n - 1):])

d = "11010011101100"
p12 = "1100000001111"
p16 = "11000000000000101"
pcc = "10001000000100001"

print("CRC-12   :", crc_remain(d, p12))
print("CRC-16   :", crc_remain(d, p16))
print("CRC-CCITT:", crc_remain(d, pcc))
