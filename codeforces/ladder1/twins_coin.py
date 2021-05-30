coins = int(input())
v = input()
vals = []
for c in v.split(' '):
    vals.append(int(c))
vals = sorted(vals, reverse=True)
total = sum(vals)
res = 0
sums = 0
for c in vals:
    sums += c
    res += 1
    if sums > int(total/2):
        print(res)
        break
