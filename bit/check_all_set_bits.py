'''
    Given a number n find all the set bits
    E.g. 13 = 1101 should return {0,2,3) as set bits. bit 1 is zero
'''
import math


def check_all_set_bits(n):
    all_set_bits = []
    i = 0
    logn = math.log(n, 2)
    while i < logn:
        if n & (1 << i):
            all_set_bits.append(i)
        i += 1
    return all_set_bits


print(check_all_set_bits(13))
