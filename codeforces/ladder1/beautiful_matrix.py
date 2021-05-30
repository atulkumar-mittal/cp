a = input().split(' ')
b = input().split(' ')
ca = input().split(' ')
d = input().split(' ')
e = input().split(' ')


i = 0
j = 0
pos = False
c = 0
for n in a:
    if int(n) == 1:
        i = 0
        j = c
        pos = True
        break
    c += 1

c = 0
if not pos:
    for n in b:
        if int(n) == 1:
            i = 1
            j = c
            pos = True
            break
        c += 1

c = 0
if not pos:
    for n in ca:
        if int(n) == 1:
            i = 2
            j = c
            pos = True
            break
        c += 1

c = 0
if not pos:
    for n in d:
        if int(n) == 1:
            i = 3
            j = c
            pos = True
            break
        c += 1

c = 0
if not pos:
    for n in e:
        if int(n) == 1:
            i = 4
            j = c
            pos = True
            break
        c += 1

res = abs(2-i) + abs(2-j)
print(res)