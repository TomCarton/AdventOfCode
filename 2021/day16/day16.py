#!/usr/bin/python3
import sys
from functools import reduce

packet_operator = [
    # Type ID 0: `sum` packet
    (lambda a, b:a + b),
    # Type ID 1: `product` packet
    (lambda a, b:a * b),
    # Type ID 2: `minimum` packet
    (lambda a, b:a if a <= b else b),
    # Type ID 3: `maximum` packet
    (lambda a, b:a if a > b else b),
    # Type ID 4: `litteral` packet
    None,
    # Type ID 5: `greater than` packet
    (lambda a, b:a > b),
    # Type ID 6: `less than` packet
    (lambda a, b:a < b),
    # Type ID 7: `equal to` packet
    (lambda a, b:a == b)
]

version_sum = 0
def value(bits): return eval(f'0b{bits}')

def parse(packet):
    global version_sum

    p = 0

    version = value(packet[p:p + 3])
    p += 3
    version_sum += version

    type = value(packet[p:p + 3])
    p += 3

    if type == 4: # literal value
        v = 0
        c = '1'
        while c == '1':
            c = packet[p]
            p += 1

            v = (v << 4) + value(packet[p:p + 4])
            p += 4

        return v, p

    else: # operator packet
        vs = []

        len_type = packet[p]=='1'
        p += 1

        if len_type == 0: # length type 0: 15 bits
            len = value(packet[p:p + 15])
            p += 15

            e = p + len
            while p < e:
                v, size = parse(packet[p:])
                vs.append(v)
                p += size

        else: # length type 1: 11 bits
            len = value(packet[p:p + 11])
            p += 11

            for _ in range(len):
                v, size = parse(packet[p:])
                vs.append(v)
                p += size

        # reduce sub-packets
        v = reduce(packet_operator[type], vs)

        return v, p

if __name__ == '__main__':
    filename = 'input.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    file = open(filename)
    lines = [line.strip() for line in file]

    bits = "".join([format('0123456789ABCDEF'.index(c), '04b') for c in lines[0]])
    val, size = parse(bits)

    # Part One:
    # What do you get if you add up the version numbers in all packets?
    print("Part One:", version_sum)

    # Part Two:
    # What do you get if you evaluate the expression represented by your hexadecimal-encoded BITS transmission?
    print("Part Two:", val)
