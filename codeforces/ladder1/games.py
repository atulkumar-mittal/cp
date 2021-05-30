n = int(input())
teams = n
colors = []
res = 0
while n > 0:
    c = input().split(" ")
    colors.append(c)
    n -= 1
i = 0
j = 0
while i < teams:
    j = i+1
    while j < teams:
        #print(' match between {} and {}: color of first {}, color of second {}'.format(i, j, colors[i], colors[j]))
        if colors[i][0] == colors[j][1]:
            res += 1
        if colors[j][0] == colors[i][1]:
            res += 1
        j += 1
    i += 1
print(res)
