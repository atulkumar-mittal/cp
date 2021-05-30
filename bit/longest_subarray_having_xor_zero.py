def func(arr):
    hashing = {}
    i = 0
    prexor = 0
    maxlen = 0
    while i < len(arr):
        prexor = prexor ^ arr[i]
        if prexor != 0 and hashing.get(prexor) is None:
            hashing[prexor] = i
        else:
            if prexor == 0:
                maxlen = max(maxlen, i + 1)
            else:
                maxlen = max(maxlen, i - hashing.get(prexor))
        print('index: {}, prexor:{}, maxlen:{}, hasing:{}'.format(i, prexor, maxlen, hashing))
        i += 1


func([6, 7, 1, 5, 3, 2, 2, 1, 2, 6, 7])
