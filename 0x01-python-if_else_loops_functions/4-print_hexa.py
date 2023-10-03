#!/usr/bin/python3

for number in range(0, 99):
    hex_value = hex(number)
    print("{:d} = 0x{:x}".format(number, number))
