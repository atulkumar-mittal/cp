inp = input().split(' ')
n = int(inp[0])
m = int(inp[1])
a = int(inp[2])
b = int(inp[3])

res = 0

res = min(int(n/m) * b, n * a)

n = n % m

if n > 0:
    if (n * a) < b:
        res += (n*a)
    else:
        res += b

print(res)