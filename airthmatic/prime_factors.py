from airthmatic.prime import is_prime
import time


def prime_factors(n):
    start = time.process_time()
    p = 2
    while p <= n:
        if n % p == 0:
            print(p)
            n = n / p
        else:
            p = get_next_prime(p)
    print("time taken by my method : {}".format(time.process_time() - start))


def get_next_prime(n):
    n += 1
    while True:
        if is_prime(n):
            return n
        n += 1


def prime_factors_gfg(n):
    start = time.process_time()
    if n <= 1:
        return
    while n % 2 == 0:
        print(2)
        n = n / 2
    while n % 3 == 0:
        print(3)
        n = n / 3
    i = 5
    while i * i <= n:
        while n % i == 0:
            print(i)
            n = n / i
        while n % (i+2) == 0:
            print(i+2)
            n = n / (i+2)
        i = i + 6
    if n > 3:
        print(n)
    print("time taken by GFG method : {}".format(time.process_time() - start))


prime_factors(13844638272628)

print("using gfg")

prime_factors_gfg(13844638272628)