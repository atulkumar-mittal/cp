def recursive_sum(i, s, arr, res):
    if i == len(arr):
        res.append(s)
        return
    recursive_sum(i + 1, s + arr[i], arr, res)
    recursive_sum(i + 1, s, arr, res)


def recursive_sum_map(i, s, arr, res_map):
    if i == len(arr):
        if res_map.get(s) is None:
            res_map[s] = 1
        else:
            res_map[s] += 1
        return
    recursive_sum_map(i + 1, s + arr[i], arr, res_map)
    recursive_sum_map(i + 1, s, arr, res_map)


def find_all_subsequences_sum(arr):
    res = []
    recursive_sum(0, 0, arr, res)
    print(res)


def find_all_subsequences_sum_map(arr):
    res = {}
    recursive_sum_map(0, 0, arr, res)
    print(res)


def find_all_subsequences_sum_using_loop(arr):
    res = []
    for i in range(len(arr)):
        res.append(arr[i])
        prev_elem_len = len(res) - 1
        for j in range(prev_elem_len):
            res.append(res[j] + arr[i])
    print(res)


find_all_subsequences_sum([1, 2, 3, 4])
find_all_subsequences_sum_map([1, 2, 3, 4])
find_all_subsequences_sum_using_loop([1,2,3,4])