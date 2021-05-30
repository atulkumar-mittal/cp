def all_divisors(n):
    bag = []
    if n == 0:
        return
    i = 1
    while i*i < n:
        if n % i == 0:
            bag.append(int(n/i))
            bag.append(i)
        i += 1
    print(sorted(bag))


all_divisors(100)