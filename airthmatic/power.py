from math import floor, ceil
import time


# Gives max depth of recursion error
def power(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    return a * power(a, b - 1)


# Works without error
def power_opt(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    return power_opt(a, floor(b / 2)) * power_opt(a, ceil(b / 2))


def power_more_opt(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    temp = power_more_opt(a, b / 2)

    if b % 2 == 0:
        return temp * temp
    else:
        return temp * temp * a


start = time.process_time()
print(power_opt(3, 2242))
print("time taken by my method : {}".format(time.process_time() - start))
start = time.process_time()
print(power_more_opt(3, 2242))
print("time taken by my method : {}".format(time.process_time() - start))
