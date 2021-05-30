def freq(a):
    print('Input array: {}'.format(a))
    count = 1
    i = 1
    while i < len(a):
        if a[i] != a[i-1]:
            print('element {}: freq {}'.format(a[i-1], count))
            count = 0
        count += 1
        i += 1
    if count > 0:
        print('element {}: freq {}'.format(a[i - 1], count))


freq([10, 10, 10, 25, 30, 30])
freq([10, 10, 10, 10])
freq([10, 20, 30])
freq([40, 10, 10, 10])