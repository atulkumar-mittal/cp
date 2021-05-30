n = int(input())
rows = []
while n > 0:
    rows.append(input().split(' '))
    n -= 1
j = 0
l = len(rows)
while j < len(rows[0]):
    i = 0
    res = 0
    while i < l:
        res += int(rows[i][j])
        i += 1
    if res != 0:
        res = 1
        break
    j+=1
if res == 0:
    print('YES')
else:
    print('NO')
