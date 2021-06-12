def func(arr):
    hashing = {}
    i = 0
    prexor = 0
    maxlen = 0
    while i < len(arr):
        prexor = prexor ^ arr[i]
        if prexor == 0:
            maxlen = i+1
        elif hashing.get(prexor) is not None:
            maxlen = max(maxlen, i - hashing.get(prexor))
        else:
            hashing[prexor] = i
        print('index: {}, prexor:{}, maxlen:{}, hasing:{}'.format(i, prexor, maxlen, hashing))
        i += 1


func([6, 7, 1, 5, 3, 2, 2, 1, 2, 6, 7])
