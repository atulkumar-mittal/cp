n = int(input())
s = input()
res = []
ns = s.split(' ')
for a in ns:
    res.append(0)
i = 0
while i < len(ns):
    res[int(ns[i])-1] = i + 1
    i += 1

for num in res:
    print(num, end=' ')