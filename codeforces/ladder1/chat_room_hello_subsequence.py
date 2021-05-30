s1 = input()
s2 = 'hello'

i = 0
j = 0

while i < len(s1) and j < 5:
    if s1[i] == s2[j]:
        j += 1
    i += 1

if j == 5:
    print('YES')
else:
    print('NO')