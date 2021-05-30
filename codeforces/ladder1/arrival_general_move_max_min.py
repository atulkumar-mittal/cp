n = int(input())
a = input().split(' ')

maxi = 0
mini = 0

i = 1
while i < len(a):
    if int(a[i]) > int(a[maxi]):
        maxi = i
    elif int(a[i]) <= int(a[mini]):
        mini = i
    i+=1

if mini < maxi:
    print(maxi + len(a)-1 - mini -1)
else:
    print(maxi + len(a)-1 - mini)