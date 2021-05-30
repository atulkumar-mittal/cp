# all the elements which are larger than all the elements to its right side
def leaders_in_array(arr):
    res = []
    max_so_far = arr[len(arr) - 1]
    res.append(max_so_far)
    j = len(arr) - 2
    while j >= 0:
        if arr[j] > max_so_far:
            max_so_far = arr[j]
            res.append(max_so_far)
        j -= 1
    print(res)


leaders_in_array([7, 10, 4, 10, 6, 5, 2])
leaders_in_array([10, 20, 30])
leaders_in_array([10, 5, 1])
