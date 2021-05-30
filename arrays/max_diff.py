# find max diff a[j] - a[i] for j > i
def find_max_diff(a):
    # handle error, null, size cases
    max_diff = a[1] - a[0]
    min_el = min(a[0], a[1])
    i = 2
    while i < len(a):
        max_diff = max(max_diff, a[i] - min_el)
        min_el = min(min_el, a[i])
        i += 1
    print(max_diff)


find_max_diff([2, 10, 1, 20, 4, 8, 1])
find_max_diff([7, 9, 5, 6, 3, 2])
find_max_diff([10, 20, 30])
find_max_diff([30, 10, 8, 2])
