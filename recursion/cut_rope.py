def cut_rope(n, a, b, c):
    if n < 0:
        return -1

    if n == 0:
        return 0

    res = max(cut_rope(n - a, a, b, c),
              cut_rope(n - b, a, b, c),
              cut_rope(n - c, a, b, c))

    if res == -1:
        return -1;

    return res + 1


ways = cut_rope(23, 11, 12, 3)
print(ways)
