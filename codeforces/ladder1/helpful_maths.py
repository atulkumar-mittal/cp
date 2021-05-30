s = input()
digits = []
res = ''
for c in s:
    if c.isdigit():
        digits.append(c)
digits = sorted(digits)
for d in digits:
    res = res + d + '+'
print(res[0:len(res)-1])