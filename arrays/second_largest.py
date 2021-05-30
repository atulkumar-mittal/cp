def second_largest(arr):
    max1 = -1
    max2 = -1
    i = 1
    if len(arr) >= 1:
        max1 = 0
    while i < len(arr):
        if arr[i] > arr[max1]:
            max2 = max1
            max1 = i
        else:
            if max2 == -1 or (arr[i] > arr[max2] and arr[i] != arr[max1]):
                max2 = i
        i += 1
    print('index of max1, max2 {},{}'.format(max1, max2))
    if max2 >= 0:
        print('max1,max2 elements of {}, {}, {}'.format(arr, arr[max1], arr[max2]))
    return max2


second_largest([10, 10, 10])  # -1 (no second largest)
second_largest([1, 2, 30, 20, 30, 29]) # 29
second_largest([-1, 0, -2, -3]) # -1
second_largest([1, 5, 4, 2]) # 4
second_largest([]) #-1
second_largest([1]) #-1
