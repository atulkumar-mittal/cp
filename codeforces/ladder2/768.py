# [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1]
'''
12--
6 0 6
3 0 3 0 3 0 3
1 1 1 0 1 1 1 0 1 1 1 0 1 1 1

101
50 1 50
25 0 25 1 25 0 25
12 1 12
6 0 6
3 0 3
1 1 1

9
4 1 4
2 0 2
1 0 1


0 = 0
1 = 0 1 0
2 = 1 0 1
3 = 1 1 1
4 = 2 0 2 => 1 0 1 0 1 0 1
9 = 4 1 4
10
'''


def merge(num, arr):
    if num <= 1:
        arr.append(num)
        return
    merge(num >> 1, arr)
    merge(num % 2, arr)
    arr.extend(arr[0:-1])


inp = input().split(" ")
n = int(inp[0])
l = int(inp[1])
r = int(inp[2])

arr = []
merge(n, arr)
ans = 0
print("merged")
print(arr)
for i in range(l-1, r):
    if arr[i] == 1:
        ans += 1

print(ans)
