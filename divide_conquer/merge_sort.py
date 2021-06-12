def sort_arr(arr):
    print('input arr {}'.format(arr))
    merge_sort(arr, 0, len(arr)-1)


def merge_sort(arr, low, high):
    if low >= high:
        return
    print('calling for low :{}, high {}'.format(low, high))
    mid = low + ((high-low) >> 1)
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid+1
    i = 0
    print('un merged original array is {}'.format(arr[low: high + 1]))
    print('left array is : {}, Right array is {}'.format(arr[low:mid+1], arr[mid+1: high+1]))
    if low > high:
        return
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
        i += 1
    while left <= mid:
        temp.append(arr[left])
        i += 1
        left += 1
    while right <= high:
        temp.append(arr[right])
        i += 1
        right += 1
    print('Merged temp array is {}'. format(temp))
    for i in range(len(temp)):
        arr[low+i] = temp[i]
    print('merged original array is {}'.format(arr[low: high+1]))


sort_arr([4, 2, 6, 2, 1, 5, 7, 9, 1,0,0,0, -1, -3])
