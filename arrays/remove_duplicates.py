def remove_dup(arr):
    # consider arr is sorted or else arr = sorted(arr)
    print("input arr {}".format(arr))
    i = 1
    insert_pos = 1
    while i < len(arr):
        if arr[i] != arr[insert_pos-1]:
            arr[insert_pos] = arr[i]
            insert_pos += 1
        i += 1
    print("modified arr {}".format(arr))


remove_dup([-1, -1, -1, 0, 0, 0, 1, 1, 1])
remove_dup([1, 2, 3, 4, 5])
remove_dup([1, 2, 2, 4, 5, 5, 5])
