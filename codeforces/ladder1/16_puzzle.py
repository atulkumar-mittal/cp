nm = input().split(' ')
m = int(nm[1])
n = int(nm[0])
sizes = input().split(' ')
pz = []
for s in sizes:
    pz.append(int(s))
pz = sorted(pz)
#print(pz)
res = pz[n-1] - pz[0]
i = 1
while i < len(pz)-n+1:
    #print('index {} and index{} , diff {}'. format(i, n+i-1, pz[n+i-1]-pz[i]))
    res = min(pz[n+i-1]-pz[i], res)
    i += 1
print(res)