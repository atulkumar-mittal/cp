n = int(input())

n1 = n
res = False

if not res:
    while n1 > 0:
        d = n1 % 10
        if d == 4 or d == 7:
            n1 = int(n1 / 10)
        else:
            break
if n1 == 0:
    res = True

if not res:
    all_lucky = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

    for d in all_lucky:
        if d < n:
            if n % d == 0:
                res = True
        else:
            break

if res:
    print('YES')
else:
    print('NO')
