from airthmatic.gcd import gcd, gcd_opt


def lcm(a, b):
    i = 1
    max_of = lm = max(a, b)
    while True:
        if lm % a == 0 and lm % b == 0:
            return lm
        i += 1
        lm = max_of * i


# a * b = lcm(a,b) * gcd(a,b) hence
def lcm_using_gcd(a, b):
    return (a * b) / gcd_opt(a, b)


print(lcm(3, 40))
print(lcm_using_gcd(3, 40))
