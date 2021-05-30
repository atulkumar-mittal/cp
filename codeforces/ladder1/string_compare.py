a = input()
b = input()
i = 0
res = 0
while i < len(a):
    if a[i].lower() < b[i].lower():
        res = -1
        break
    elif a[i].lower() > b[i].lower():
        res = 1
        break
    i += 1
print(res)