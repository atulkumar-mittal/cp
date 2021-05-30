def move_zeros(arr):
    print('before: {}'.format(arr))
    first_zero = -1
    i = 0
    while i < len(arr):
        if arr[i] == 0 and first_zero == -1:
            first_zero = i
        if arr[i] != 0 and first_zero != -1:
            arr[first_zero] = arr[i]
            arr[i] = 0

            j = first_zero   # after copying the first zero may or may not be first_zero+1.
            # So move until we find the first_zero
            while arr[j] != 0:
                j += 1
            first_zero = j
        i += 1
    print('after: {}'.format(arr))


def move_zeros_efficient(arr):
    print('before efficient: {}'.format(arr))
    count_non_zero = 0
    i = 0
    while i < len(arr):
        if arr[i] != 0:
            swap(i, count_non_zero, arr)
            count_non_zero += 1
        i += 1
    print('after efficient: {}'.format(arr))


def swap(a, b, arr):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


move_zeros([8, 5, 0, 10, 0, 20])
move_zeros([0, 0, 0, 0, 10, 0])
move_zeros([10, 20])
move_zeros([-1, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 0, 0, 0, 0, 6])

move_zeros_efficient([8, 5, 0, 10, 0, 20])
move_zeros_efficient([0, 0, 0, 0, 10, 0])
move_zeros_efficient([10, 20])
move_zeros_efficient([-1, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 0, 0, 0, 0, 6])
