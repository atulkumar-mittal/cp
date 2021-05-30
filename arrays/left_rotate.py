def left_rotate(arr, n):
    l = len(arr)
    n = n % l  # if n is greater than length, the effective rotation is actually n%l
    brr = [0] * l
    i = 0
    while i < l:
        target = (l + i - n) % l
        brr[target] = arr[i]
        i += 1
    print(brr)


left_rotate([1,2,4,5], 2)