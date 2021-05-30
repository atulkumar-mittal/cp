def find_kth_bit(n, k):
    i = 0
    while n > 0 and i != k:
        i += 1
        if i == k:
            return int(n % 2)
        n = int(n / 2)
    return 0


def find_kth_bit_using_leftshift(n, k):
    return (n & (1 << k - 1)) != 0


b = find_kth_bit_using_leftshift(2, 1)
print(b)
