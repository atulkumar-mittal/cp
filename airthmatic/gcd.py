def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b;
        else:
            b = b - a;
    return a


def gcd_opt(a, b):
    if b == 0:
        return a
    return gcd_opt(b, a % b)


print(gcd(10, 24))
print(gcd_opt(10, 24))
