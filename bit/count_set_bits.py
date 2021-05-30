def count_set_bits(n):
    count = 0
    while n != 0:
        if (n & 1) > 0:
            count += 1
        n = n >> 1
    return count


def count_set_bits_brian_kerningam(n):
    count = 0
    while n > 0:
        n = n & (n - 1)     # 4 = 100, 3 = 011 bitwise & will make left most bit 0. This is true for all n and n-1
        count += 1
    return count


print(count_set_bits_brian_kerningam(7))