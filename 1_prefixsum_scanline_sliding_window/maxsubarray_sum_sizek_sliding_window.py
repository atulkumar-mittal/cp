'''
Given an array of size n, we need to find the maximum sum of size k
'''


def give_max_sum_size_k(arr, k):
    if len(arr) == 0 or k > len(arr):
        return 0

    # find first sliding window sum
    maxi = 0
    for i in range(k):
        maxi += arr[i]

    current_sum = maxi
    left = 0
    right = k
    for i in range(1, len(arr) - k + 1):
        current_sum += arr[right]
        current_sum -= arr[left]
        maxi = max(maxi, current_sum)
        left += 1
        right += 1

    return maxi


maxi = give_max_sum_size_k([1, 2, 3, 7, 3, 99, 1, 24, 4, -123], 5)
print(maxi)
