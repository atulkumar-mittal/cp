def printdfs(i, n):
    if i > n:
        return
    print(i)
    for j in range(0, 10):
        printdfs(i*10+j, n)


for i in range(1, 10):
    printdfs(i, 1000)