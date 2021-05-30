def is_odd_num(n):
    return n & 1


# 13 = 1101 so bits are 3,2,1,0  first bit starts from zero
def is_ith_bit_set(n, i):
    return (n >> i) & 1 or n & (1 << i)


def set_ith_bit(n, i):
    return n | (1 << i)


def unset_ith_bit(n, i):
    return n ^ (1 << i)


def check_number_is_power_of_2(n):
    return (n &
            (n - 1)) == 0
